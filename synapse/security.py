from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from .config import settings

API_KEY_NAME = "X-API-KEY"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def api_key_security(key: str = Security(api_key_header)):
    """
    Dependency to verify the API key in the request header.
    """
    if key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="An API key is required. Please include it in the 'X-API-KEY' header."
        )
    if key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The provided API key is not valid."
        )
    return True
