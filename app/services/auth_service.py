from sqlalchemy.orm import Session
from jose import JWTError

from app.models.user import User
from app.schemas.user import UserRegister, UserLogin
from app.utils.security import hash_password, verify_password
from app.utils.jwt_handler import create_access_token, verify_token


def register_user(user: UserRegister, db: Session):
    existing_email = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_email:
        raise ValueError("Email already registered")

    existing_username = (
        db.query(User)
        .filter(User.username == user.username)
        .first()
    )

    if existing_username:
        raise ValueError("Username already taken")

    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(
        {
            "sub": str(new_user.id),
            "email": new_user.email,
        }
    )

    return {
        "user": new_user,
        "access_token": token,
        "token_type": "bearer",
    }


def login_user(user: UserLogin, db: Session):
    db_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not db_user:
        raise ValueError("Invalid email or password")

    if not verify_password(
        user.password,
        db_user.hashed_password,
    ):
        raise ValueError("Invalid email or password")

    token = create_access_token(
        {
            "sub": str(db_user.id),
            "email": db_user.email,
        }
    )

    return {
        "user": db_user,
        "access_token": token,
        "token_type": "bearer",
    }


def get_current_user(token: str, db: Session):
    try:
        payload = verify_token(token)

        user_id = payload.get("sub")

        if user_id is None:
            return None

    except JWTError:
        return None

    return (
        db.query(User)
        .filter(User.id == int(user_id))
        .first()
    )