import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.constants.constants import LLAMA_URL
from server.models.ChatRequest import ChatRequest
from server.services.ChatService import ChatService as ChatService
from server.services.HealthCheckService import HealthCheckService as HealthCheckService

app = FastAPI(root_path="/chat/api")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def healthCheck() -> dict:
    return await HealthCheckService.healthCheck()


@app.post("/send-chat")
async def sendChat(chatRequest: ChatRequest) -> dict:
    return await ChatService.sendChat(chatRequest.userMsg)


print(f"LLAMA url is: {LLAMA_URL}")

if __name__ == "__main__":
    uvicorn.run(app="app:app")
