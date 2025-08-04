from pydantic import BaseModel, Field

class Book(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    available: bool = True

class Member(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)

class BorrowRequest(BaseModel):
    book_id: int = Field(..., gt=0)
    member_id: int = Field(..., gt=0)