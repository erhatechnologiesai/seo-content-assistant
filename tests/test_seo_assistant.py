import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestSEOAssistant(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_brief_generation(self):
        res = self.client.post("/generate-seo-brief", json={"primary_keyword": "RAG vector pipeline", "target_intent": "informational"})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("vector pipeline", data["recommended_title"].lower())
        self.assertGreater(len(data["suggested_h2_headers"]), 2)

if __name__ == "__main__":
    unittest.main()
