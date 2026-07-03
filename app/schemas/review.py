from datetime import datetime

from pydantic import BaseModel, Field, field_validator


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
    max_length=20000,
    description="Source code to be reviewed (maximum 20,000 characters)",
    example="print('Hello World')"
)

    @field_validator("language")
    @classmethod
    def clean_language(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Language cannot be empty")

        return value

    @field_validator("code")
    @classmethod
    def reject_blank_code(cls, value: str) -> str:
        if not value.strip():
            raise ValueError(
                "Code cannot be empty or contain only whitespace"
            )

        return value


class ReviewUpdate(BaseModel):

    review: str = Field(
        ...,
        min_length=1,
        description="Updated review text"
    )

    score: int = Field(
        ...,
        ge=0,
        le=10,
        description="Updated review score"
    )
    @field_validator("review")
    @classmethod
    def reject_blank_review(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError(
            "Review cannot be empty or contain only whitespace"
        )

        return value


class ReviewResponse(BaseModel):

    id: int
    language: str
    code: str
    review: str
    score: int
    created_at: datetime

    class Config:
        from_attributes = True