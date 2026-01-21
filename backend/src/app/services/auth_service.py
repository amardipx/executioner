from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.domain import User
from app.utils.security import hash_password, verify_password


async def create_user(
    db: AsyncSession, username: str, password: str
) -> User:
    user = User(
        username=username,
        password_hash=hash_password(password),
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def authenticate_user(
    db: AsyncSession, username: str, password: str
) -> User | None:
    result = await db.execute(
        select(User).where(User.username == username)
    )
    user = result.scalar_one_or_none()

    if not user:
        return None

    if not verify_password(password, user.password_hash):
        return None

    return user
