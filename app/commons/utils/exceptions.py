from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

CredentialsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
)

UnauthorizedException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)


class InvalidLdapServerCredentials(Exception):
    pass


class LdapException(Exception):
    pass
