from fastapi import FastAPI
from google.adk.runtime.fastapi import mount_agent
from agent import build

app = FastAPI()

agent = build()
mount_agent(app, agent)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
