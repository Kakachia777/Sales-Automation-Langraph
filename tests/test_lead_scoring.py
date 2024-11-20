import pytest
from src.tools.lead_scorer import score_lead
from src.config.settings import Settings

settings = Settings()

@pytest.fixture
def sample_company_profile():
    return {
        "company_name": "TechCorp",
        "company_location": ["United States"],
        "company_industry": ["Technology"],
        "company_size": "20-50"
    }

@pytest.fixture
def sample_open_positions():
    return ["Customer Support Manager", "Technical Support Specialist"]

def test_lead_scoring(sample_company_profile, sample_open_positions):
    score = score_lead(sample_company_profile, sample_open_positions)
    assert isinstance(score, int)
    assert 0 <= score <= 100
    
def test_lead_qualification(sample_company_profile, sample_open_positions):
    score = score_lead(sample_company_profile, sample_open_positions)
    assert score >= settings.MIN_QUALIFIED_SCORE 