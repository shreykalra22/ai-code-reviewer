from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    Query,
    status
)
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.review import (
    ReviewCreate,
    ReviewResponse,
    ReviewUpdate
)
from app.services.review_service import (
    AIReviewError,
    GeminiInvalidResponseError,
    GeminiUnavailableError,
    delete_review,
    get_review_by_id,
    get_reviews,
    review_code,
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
    try:
        return review_code(
            db=db,
            language=review.language,
            code=review.code
        )

    except GeminiUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc)
        ) from exc

    except GeminiInvalidResponseError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc)
        ) from exc

    except AIReviewError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc)
        ) from exc


@router.get(
    "/reviews",
    response_model=list[ReviewResponse]
)
def read_reviews(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
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
    review_id: int = Path(..., ge=1),
    db: Session = Depends(get_db)
):
    review = get_review_by_id(
        db=db,
        review_id=review_id
    )

    if review is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
        )

    return review


@router.delete(
    "/reviews/{review_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_review_endpoint(
    review_id: int = Path(..., ge=1),
    db: Session = Depends(get_db)
):
    review = delete_review(
        db=db,
        review_id=review_id
    )

    if review is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
        )

    return None


@router.put(
    "/reviews/{review_id}",
    response_model=ReviewResponse
)
def update_review_endpoint(
    request: ReviewUpdate,
    review_id: int = Path(..., ge=1),
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
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
        )

    return review