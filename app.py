from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")

with open("events.json", "r") as f:
    events = json.load(f)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, size: str = None):
    filtered_events = events
    if size == "small":
        filtered_events = [event for event in events if event["size"] == "small"]
    elif size == "big":
        filtered_events = [event for event in events if event["size"] == "big"]
    return templates.TemplateResponse("index.html", {"request": request, "events": filtered_events})

