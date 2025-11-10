from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
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
        # If the response is a report, we need to convert the path to a download URL
        if response.get("type") == "report":
            # Construct the full download URL
            file_path = response.get("path", "")
            download_url = f"http://127.0.0.1:8000/{file_path}"
            response["download_url"] = download_url
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Medical Report Agent Backend! Use /ask_agent/ to interact with the agent."}


@app.get("/reports/{filename}")
async def download_report(filename: str):
    """
    Endpoint to download a generated report.
    """
    file_path = f"reports/{filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)
