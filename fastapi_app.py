from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from evaluation.deepeval_eval import run_deepeval
import uvicorn
import os

from itsupportbot.retrieval_generation import generation
from itsupportbot.ingest import ingestdata

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Load vector store and generation chain
vstore = ingestdata("done")
chain = generation(vstore)

# Mount templates and static directories
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Root route - renders the HTML chat page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

# Chat endpoint (handles both GET and POST)
@app.post("/get")
async def chat(msg: str = Form(...)):
    input_text = msg

    # Invoke the chain with user input
    result = chain.invoke(input_text)
    print("Response:", result)
    return result


@app.get("/ask")
async def ask(query: str = Query(..., description="Your support query")):
    """
    Simple GET endpoint: /ask?query=your question
    Returns plain text response from RAG model.
    """
    result = chain.invoke(query)
    
    # If result is a dict or object, convert to string
    if isinstance(result, dict):
        return result.get("text", str(result))
    return str(result)


if __name__ == "__main__":
    uvicorn.run("fastapi_app:app", host="0.0.0.0", port=8080, reload=True)
