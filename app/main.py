from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Project AI App!"}

@app.get("/status")
def status():
    return {"status": "running"}

