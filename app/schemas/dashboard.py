from pydantic import BaseModel


class WeeklyReview(BaseModel):
    day: str
    count: int


class RecentReview(BaseModel):
    id: int
    language: str
    score: int
    created_at: str


class DashboardResponse(BaseModel):
    total_reviews: int
    average_score: float
    production_ready: int

    languages: dict[str, int]

    weekly_reviews: list[WeeklyReview]

    recent_reviews: list[RecentReview]

    top_issues: list[str]