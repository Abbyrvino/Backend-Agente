from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.agent.main import run_agent

app = FastAPI()


class UserRequest(BaseModel):
    prompt: str


@app.post("/ask_agent/")
async def ask_agent(request: UserRequest):
    """
    Endpoint to send a natural language prompt to the intelligent agent.
    """
    try:
        response = run_agent(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Medical Report Agent Backend! Use /ask_agent/ to interact with the agent."}
