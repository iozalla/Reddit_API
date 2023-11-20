# models.py
from pydantic import BaseModel
from typing import List, Optional

class SearchRequest(BaseModel):
    subreddit: str
    keyword: str
    sort: str
    time_filter: str
    limit: int

class ImageResolution(BaseModel):
    url: str
    width: int
    height: int

class SearchResult(BaseModel):
    title: str
    url: str
    score: int
    created_utc: float
    body: Optional[str] = None
    image_urls: List[ImageResolution] = []
    author: Optional[str] = None
    comments_count: int

class SearchResponse(BaseModel):
    results: List[SearchResult]
