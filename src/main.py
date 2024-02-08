from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from vocabulary.word import read_vocabulary

app = FastAPI()


templates = Jinja2Templates(directory="templates")


@app.get("/vocabulary", response_class=HTMLResponse)
async def vocabulary(request: Request):
    words = read_vocabulary()
    return templates.TemplateResponse(
        request=request, name="vocabulary.html", context={"words": words}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
