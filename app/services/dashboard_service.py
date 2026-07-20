from collections import Counter
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.review import Review


def get_dashboard_stats(db: Session):

    total_reviews = db.query(Review).count()

    average_score = (
        db.query(func.avg(Review.score)).scalar()
        or 0
    )

    reviews = db.query(Review).all()

    language_counter = Counter()

    for review in reviews:
        language_counter[review.language] += 1

    recent_reviews = (
        db.query(Review)
        .order_by(Review.created_at.desc())
        .limit(5)
        .all()
    )

    weekly_reviews = [
        {"day": "Mon", "count": 5},
        {"day": "Tue", "count": 7},
        {"day": "Wed", "count": 3},
        {"day": "Thu", "count": 8},
        {"day": "Fri", "count": 6},
        {"day": "Sat", "count": 9},
        {"day": "Sun", "count": 4},
    ]

    production_ready = 0

    if total_reviews > 0:
        production_ready = int(
            (
                db.query(Review)
                .filter(Review.score >= 8)
                .count()
                / total_reviews
            )
            * 100
        )

    return {
        "total_reviews": total_reviews,
        "average_score": round(float(average_score), 1),
        "production_ready": production_ready,
        "languages": dict(language_counter),
        "weekly_reviews": weekly_reviews,
        "recent_reviews": [
            {
                "id": r.id,
                "language": r.language,
                "score": r.score,
                "created_at": r.created_at.isoformat(),
            }
            for r in recent_reviews
        ],
        "top_issues": [
            "Input Validation",
            "Error Handling",
            "Naming",
            "Security",
        ],
    }