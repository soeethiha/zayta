from typing import Annotated, List, Any, Tuple, Iterable, cast
import ldap
from ldap.filter import filter_format

from models.user import Login
from config.config import config
from commons.utils.exceptions import InvalidLdapServerCredentials, LdapException

URI = f'ldap://{config.ldap_server}:{config.ldap_server_port}'

QueryResult = Annotated[List[Tuple[None, None, List[None]]]
                        | Any | None, 'LDAP Query Result']


class AuthLdap:
    @staticmethod
    def _connect():
        connection = ldap.initialize(URI)
        if config.ldap_chase_ref_disabled:

            connection.set_option(
                ldap.OPT_REFERRALS,  # pyright: ignore[reportGeneralTypeIssues]
                ldap.OPT_OFF  # pyright: ignore[reportGeneralTypeIssues]
            )
        if config.ldap_tls:
            connection.start_tls_s()

        return connection

    def _query(self, ldap_filter: str) -> QueryResult:
        results = []
        try:
            conn = self._connect()
            conn.simple_bind_s(config.ldap_binddn, config.ldap_password)
            results = conn.search_st(
                base=config.ldap_base,
                scope=ldap.SCOPE_SUBTREE, # pyright: ignore[reportGeneralTypeIssues]
                filterstr=ldap_filter, timeout=60
            )
            conn.unbind()

        except ldap.INVALID_CREDENTIALS: # pyright: ignore[reportGeneralTypeIssues]
            raise InvalidLdapServerCredentials('LDAP bind failed.')
        except ldap.LDAPError as e:  # pyright: ignore[reportGeneralTypeIssues]
            raise LdapException('An LDAP exception occurred: %s', e)

        return results

    @staticmethod
    def _get_filter(user_name) -> str:
        ldap_filter = None
        try:
            ldap_filter = filter_format(config.ldap_filter, (user_name,))
        except TypeError:
            raise ValueError(
                'Could not format LDAP filter. Your filter should contain one \'%s\'.'
            )

        return ldap_filter

    def _get_entry(self, user_name: str) -> Tuple:
        ldap_filter, dn, entry = self._get_filter(
            user_name=user_name), False, False
        results = cast(Iterable, self._query(ldap_filter))
        # Get rid of (None, attrs) for searchResultReference replies
        results = [i for i in results if i[0]]

        if len(results) == 1:
            entry = results[0]
            dn = results[0][0]

            if not dn:
                raise ValueError('Unable to get LDAP Entry. No dn value.')

        return (dn, entry)

    def auth(self, login: Login):
        dn, entry = self._get_entry(login.username)
        try:
            conn = self._connect()
            conn.simple_bind_s(dn, login.password)
            conn.unbind()

        except ldap.INVALID_CREDENTIALS: # pyright: ignore[reportGeneralTypeIssues]
            raise InvalidLdapServerCredentials('Wrong User Name or Password.')
        except ldap.LDAPError as e:  # pyright: ignore[reportGeneralTypeIssues]
            raise LdapException('An LDAP exception occurred: %s', e)

        return entry
