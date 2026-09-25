def build_seo_brief(keyword: str, intent: str):
    title = f"{keyword.title()}: Enterprise Guide & Architecture Blueprint"
    meta = f"Complete guide to {keyword}. Explore implementation patterns, latency benchmarks, and multi-agent best practices."
    secondary = [f"{keyword} best practices", f"{keyword} tools", f"enterprise {keyword}"]
    headers = [
        f"What is {keyword.title()}?",
        "Key Architectural Trade-offs",
        "Step-by-Step Implementation Framework",
        "Production Performance & Security Considerations"
    ]
    faqs = [
        {"question": f"Why is {keyword} critical for modern engineering teams?", "answer": f"{keyword.title()} eliminates manual operational overhead and accelerates cycle times."},
        {"question": "How quickly can it be deployed in production?", "answer": "Typical deployment takes 1-2 weeks using standardized automation nodes."}
    ]
    return title, meta, secondary, headers, faqs
