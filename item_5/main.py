from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Text(BaseModel):
    text: str

@app.post("/summarize/")
async def summarize_text(text: Text) -> Dict[str, str]:
    words = text.text.split()
    summary = ' '.join(words[:100])  # Simplistic approach to return first 100 words
    return {"summary": summary}

@app.post("/token-count/")
async def token_count(text: Text) -> Dict[str, int]:
    tokens = text.text.split()
    return {"token_count": len(tokens)}