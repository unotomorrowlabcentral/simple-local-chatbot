import json
import httpx
from pydantic import BaseModel

from ..constants.constants import LLAMA_URL


class Chat(BaseModel):
    model: str = "llama3.2"
    stream: bool = False
    prompt: str


class ChatService:
    @staticmethod
    async def sendChat(userMsg: str) -> dict:
        data = Chat(prompt=userMsg).model_dump()

        try:
            send = httpx.post(
                LLAMA_URL,
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=120,
            )

            responseLines = [line for line in send.text.strip().split("\n") if line]
            responseDict = [json.loads(line) for line in responseLines]

            responseStr = "".join(pair.get("response", "") for pair in responseDict)

            return {"bot_response": responseStr}

        except Exception as e:
            print(f"an error occurred: {e}")
            return {"error": str(e)}
