from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import google.generativeai as genai
from pydantic import BaseModel
import os

# Load your Gemini API key
genai.configure(api_key="AIzaSyAyO7L6SBjzhImODOkWU7WjFVjZYa85_gM")

# Define model name
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

class Query(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("index.html", "r", encoding="utf-8") as file:
        return file.read()

@app.post("/ask")
async def ask_ai(data: Query):
    try:
        response = model.generate_content(data.message)
        return {"response": response.text}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
