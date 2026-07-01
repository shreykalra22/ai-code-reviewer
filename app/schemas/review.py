from datetime import datetime

from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):

    language: str = Field(
        ...,
        min_length=2,
        max_length=20,
        description="Programming language of the submitted code",
        example="Python"
    )

    code: str = Field(
        ...,
        min_length=1,
        description="Source code to be reviewed",
        example="print('Hello World')"
    )


class ReviewResponse(BaseModel):

    id: int

    language: str

    code: str

    review: str

    score: int

    created_at: datetime

    class Config:
        from_attributes = True