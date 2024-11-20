from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # API Keys
    HUBSPOT_API_KEY: str
    RAPIDAPI_KEY: str
    SERPER_API_KEY: str
    GROQ_API_KEY: str
    
    # LLM Settings
    DEFAULT_LLM_MODEL: str = "groq/llama-3.1-70b-versatile"
    LLM_TEMPERATURE: float = 0.1
    
    # Lead Scoring
    MIN_QUALIFIED_SCORE: int = 50
    TARGET_INDUSTRIES: List[str] = ["Technology", "Accounting", "Finance"]
    
    # Location Scoring
    LOCATION_SCORES = {
        "US_EUROPE": 30,
        "OTHER": 10
    }
    
    # Company Size Scoring
    COMPANY_SIZE_SCORES = {
        "0-20": 20,
        "20-50": 15,
        "50+": 10
    }
    
    class Config:
        env_file = ".env" 