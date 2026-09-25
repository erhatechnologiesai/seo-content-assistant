from fastapi import FastAPI
from app.config import settings
from app.models import SEOBriefRequest, SEOBriefResponse
from app.services.seo_optimizer import build_seo_brief

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/generate-seo-brief", response_model=SEOBriefResponse)
def generate_brief(req: SEOBriefRequest):
    t, m, sec, h2s, faqs = build_seo_brief(req.primary_keyword, req.target_intent)
    return SEOBriefResponse(
        primary_keyword=req.primary_keyword,
        recommended_title=t,
        meta_description=m,
        secondary_keywords=sec,
        suggested_h2_headers=h2s,
        faq_schema=faqs
    )
