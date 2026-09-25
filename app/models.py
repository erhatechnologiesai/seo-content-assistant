from pydantic import BaseModel
from typing import List

class SEOBriefRequest(BaseModel):
    primary_keyword: str
    target_intent: str = "informational" # informational, transactional, commercial

class SEOBriefResponse(BaseModel):
    primary_keyword: str
    recommended_title: str
    meta_description: str
    secondary_keywords: List[str]
    suggested_h2_headers: List[str]
    faq_schema: List[dict]
