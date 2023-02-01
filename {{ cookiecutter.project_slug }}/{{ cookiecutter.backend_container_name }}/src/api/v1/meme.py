from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from src.db.session import get_session
from src.models.meme import Meme
from src.schemas.common import IGetResponseBase
from src.schemas.meme import IMemeRead


router = APIRouter()


@router.get(
    "/memes",
    response_description="List all meme instances",
    response_model=IGetResponseBase[IMemeRead],
    tags=["memes"],
)
async def memes(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1),
    session: AsyncSession = Depends(get_session),
) -> IGetResponseBase[IMemeRead]:
    result = await session.execute(
        select(Meme).offset(skip).limit(limit).order_by(Meme.created_at.desc())
    )
    memes = result.scalars().all()

    return IGetResponseBase[IMemeRead](data=memes)
