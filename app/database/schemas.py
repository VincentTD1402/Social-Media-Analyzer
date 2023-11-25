from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class DataCrawlSchema(BaseModel):
    id: str
    author: str
    title: Optional[str] = None
    content: str
    rating: Optional[int] = None
    source: str
    crawl_at: datetime = None

    class Config:
        orm_mode = True