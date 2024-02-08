from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from data.word import read_vocabulary, Word
from data.category import Category, CATEGORY_ALL
from fastapi.staticfiles import StaticFiles


app = FastAPI()


templates = Jinja2Templates(directory="templates")
app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/vocabulary", response_class=HTMLResponse)
async def vocabulary(request: Request):
    words: list[Word] = read_vocabulary() # this should be cached
    categories: list[Category] = list(set(Category(name=word.category) for word in words))
    categories = [Category(name=CATEGORY_ALL)] + categories # This should be extracted in its own logic method with a unit test
    return templates.TemplateResponse(
        request=request, name="vocabulary.html", context={"categories": categories, "words": []}
    )

@app.get("/vocabulary/{category}", response_class=HTMLResponse)
async def vocabulary(request: Request, category: str):
    words: list[Word] = read_vocabulary()  # this should be cached
    if category != CATEGORY_ALL:
        words = [word for word in words if word.category == category]
    return templates.TemplateResponse(
        request=request, name="vocabulary.html", context={"categories": [], "words": words}
    )

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="home.html"
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
