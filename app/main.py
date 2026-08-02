from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.agents.personal_agent import create_agent
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Personal Agent API")

# Configure CORS
origins = [
    "http://localhost:5173",
    "https://prakashrajput.com",
    "https://www.prakashrajput.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent, resume_context = create_agent()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    try:
        inputs = {
            "messages": [query.question],
            "resume_context": resume_context
        }
        result = agent.invoke(inputs)
        return {"answer": result["messages"][-1]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.options("/ask")
async def ask_options():
    return {
        "allowed_methods": ["POST", "OPTIONS"],
        "payload_format": {"question": "string"},
        "description": "Send a professional query to the personal agent."
    }

@app.get("/")
async def root():
    return {"message": "Personal Agent is running"}

@app.get("/health-check")
async def root():
    return {"message": "Personal Agent is running"}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
