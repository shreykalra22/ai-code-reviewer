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