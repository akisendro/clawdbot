from fastapi import FastAPI
from pydantic import BaseModel
import os
from anthropic import Anthropic

app = FastAPI()

client = Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)

class Prompt(BaseModel):
    message: str

@app.post("/ask")
def ask(prompt: Prompt):
    response = client.messages.create(
        model="claude-3-sonnet",
        max_tokens=500,
        messages=[
            {"role": "user", "content": prompt.message}
        ]
    )
    return {"reply": response.content[0].text}
