from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.user import UserLogin, UserRegister
from app.services.auth_service import login_user, register_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    try:
        result = register_user(user, db)

        return {
            "user": UserResponse.model_validate(result["user"]),
            "access_token": result["access_token"],
            "token_type": result["token_type"],
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    try:
        result = login_user(user, db)

        return {
            "user": UserResponse.model_validate(result["user"]),
            "access_token": result["access_token"],
            "token_type": result["token_type"],
        }

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )


from app.schemas.user import UserResponse

@router.get(
    "/me",
    response_model=UserResponse,
)
def me(
    current_user: User = Depends(get_current_user),
):
    return current_user