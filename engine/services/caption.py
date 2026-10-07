"""
InstaFlow — AI Caption Generation
Uses Google Gemini to generate unique Hinglish captions per account.
Each caption is natural, human-sounding, and unique across the batch.
"""

import asyncio
import httpx

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash:generateContent"


async def generate_caption(original_caption: str, account_index: int) -> str:
    """
    Generate one unique caption for a single account.
    Sounds like a real Indian person aged 18-28.
    Mix of Hindi, English, and Hinglish depending on context.
    """
    pass


async def generate_all_captions(base_caption: str, count: int) -> list[str]:
    """
    Generate `count` unique captions in parallel batches.
    Falls back to numbered variants if Gemini is unavailable.
    """
    pass
