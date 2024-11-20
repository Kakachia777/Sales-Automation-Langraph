import aiohttp
import asyncio
from typing import Dict, Optional
from ..utils.decorators import rate_limit, cache_response

class LinkedInService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com"
        }
    
    @rate_limit(calls=10, period=60)
    @cache_response(ttl=3600)
    async def get_profile(self, linkedin_url: str) -> Optional[Dict]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile",
                headers=self.headers,
                params={"linkedin_url": linkedin_url}
            ) as response:
                if response.status == 200:
                    return await response.json()
                return None 