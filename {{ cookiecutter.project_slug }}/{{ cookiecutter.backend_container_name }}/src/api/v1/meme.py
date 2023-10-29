from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.enums import SortOrder
from src.db.session import get_session
from src.repositories.meme import MemeRepository
from src.schemas.common import IGetResponseBase
from src.schemas.meme import IMemeRead


router = APIRouter()


@router.get(
    "/memes",
    response_description="List all meme instances",
    response_model=IGetResponseBase[List[IMemeRead]],
    tags=["memes"],
)
async def memes(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1),
    sort_field: Optional[str] = "created_at",
    sort_order: Optional[str] = SortOrder.DESC,
    session: AsyncSession = Depends(get_session),
) -> IGetResponseBase[List[IMemeRead]]:
    meme_repo = MemeRepository(db=session)
    memes = await meme_repo.all(
        skip=skip, limit=limit, sort_field=sort_field, sort_order=sort_order
    )

    return IGetResponseBase[List[IMemeRead]](data=memes)  # type: ignore
