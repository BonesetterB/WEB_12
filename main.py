from fastapi import FastAPI
from src.routes import contacts
import uvicorn

app= FastAPI()

app.include_router(contacts.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", reload=True, log_level="info")