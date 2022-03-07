from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from basic_auth import tokens, schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return tokens.verify_token(data, credentials_exception)


def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    if current_user.id:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


