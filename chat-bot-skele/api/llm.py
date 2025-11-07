from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI(title="Ollama Chat API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Message(BaseModel):
    message: str
    session_id: str = "default"


class OllamaChat:
    def __init__(self, model="llama3.2", host="http://localhost:11434"):
        self.model = model
        self.host = host
        self.sessions = {}

    def chat(self, user_message: str, session_id: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = []

        self.sessions[session_id].append(
            {"role": "user", "content": user_message})

        payload = {
            "model": self.model,
            "messages": self.sessions[session_id],
            "stream": False
        }

        response = requests.post(f"{self.host}/api/chat", json=payload)

        if response.status_code == 200:
            reply = response.json()["message"]["content"]
            self.sessions[session_id].append(
                {"role": "assistant", "content": reply})
            return reply
        else:
            raise HTTPException(
                status_code=response.status_code, detail=response.text)


chatbot = OllamaChat()


@app.post("/chat")
def chat_with_bot(msg: Message):
    reply = chatbot.chat(msg.message, msg.session_id)
    return {"reply": reply}


@app.get("/")
def root():
    return {"message": "Ollama Chat API is running!"}
