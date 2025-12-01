import os
from dotenv import load_dotenv
from google.adk.agents import AgentBuilder
from google.adk.messages import TextMessage, BinaryMessage
from utils.analyzer import analyze_image

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash")

def build():
    agent = AgentBuilder("image-integrity-agent", model=MODEL_NAME)

    @agent.on_text
    def on_text(context, msg: TextMessage):
        return f"Send an image to analyze integrity. Received text: {msg.text}"

    @agent.on_binary
    def on_binary(context, msg: BinaryMessage):
        image_bytes = msg.data
        result = analyze_image(image_bytes)
        return result

    return agent.build()
