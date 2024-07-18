from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class TextRequest(BaseModel):
    text: str

summarizer = pipeline("summarization")

@app.post("/summarize")
async def summarize_text(request: TextRequest):
    try:
        summary = summarizer(request.text, max_length=100, min_length=30, do_sample=False)
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/token_count")
async def count_tokens(request: TextRequest):
    try:
        tokens = request.text.split()
        return {"token_count": len(tokens)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
