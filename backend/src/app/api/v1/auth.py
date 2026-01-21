from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.pool import get_db
from app.models.schemas import UserCreate, UserLogin, TokenResponse
from app.services.auth_service import create_user, authenticate_user
from app.utils.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=TokenResponse)
async def signup(
    data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    user = await create_user(db, data.username, data.password)
    token = create_access_token(str(user.id))
    return {"access_token": token}



@router.post("/login", response_model=TokenResponse)
async def login(
    data: UserLogin,
    db: AsyncSession = Depends(get_db),
):
    user = await authenticate_user(db, data.username, data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    token = create_access_token(str(user.id))
    return {"access_token": token}
