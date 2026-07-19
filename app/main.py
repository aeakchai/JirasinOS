from pathlib import Path
import subprocess

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.file_search import search_files

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.get("/search", response_class=HTMLResponse)
def search(request: Request, keyword: str = ""):

    results = search_files(keyword)

    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={
            "keyword": keyword,
            "results": results
        }
    )


@app.get("/open")
def open_file(path: str):

    subprocess.Popen(["explorer", path])

    return RedirectResponse("/", status_code=302)


@app.get("/folder")
def open_folder(path: str):

    p = Path(path)

    subprocess.Popen(["explorer", "/select,", str(p)])

    return RedirectResponse("/", status_code=302)