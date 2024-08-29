from fastapi import Header, HTTPException
from typing import Optional

fake_users_db = {
    "user1": {"username": "user1", "password": "password1"},
    "user2": {"username": "user2", "password": "password2"}
}


def get_current_user(auth_header: Optional[str] = Header(None)):
    if auth_header is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    try:
        username, password = auth_header.split(":")
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user = fake_users_db.get(username)
    if not user or user['password'] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
