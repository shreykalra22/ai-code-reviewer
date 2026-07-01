from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import status
from app.database import get_db
from app.schemas.review import (
    ReviewCreate,
    ReviewResponse,
    ReviewUpdate
)
from fastapi import APIRouter, Depends, HTTPException, status
from app.services.review_service import (
    review_code,
    get_reviews,
    get_review_by_id,
    delete_review,
    update_review,
)

router = APIRouter()


@router.post(
    "/review",
    status_code=status.HTTP_201_CREATED
)
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):
    return review_code(
        db=db,
        language=review.language,
        code=review.code
    )


@router.get(
    "/reviews",
    response_model=list[ReviewResponse]
)
def read_reviews(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return get_reviews(
        db=db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/reviews/{review_id}",
    response_model=ReviewResponse
)
def read_review(
    review_id: int,
    db: Session = Depends(get_db)
):
    review = get_review_by_id(
        db=db,
        review_id=review_id
    )

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review
@router.delete(
    "/reviews/{review_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_review_endpoint(
    review_id: int,
    db: Session = Depends(get_db)
):
    review = delete_review(
        db=db,
        review_id=review_id
    )

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return
@router.put(
    "/reviews/{review_id}",
    response_model=ReviewResponse
)
def update_review_endpoint(
    review_id: int,
    request: ReviewUpdate,
    db: Session = Depends(get_db)
):
    review = update_review(
        db=db,
        review_id=review_id,
        review_text=request.review,
        score=request.score
    )

    if review is None:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    return review