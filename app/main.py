from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import os
import subprocess

from app.file_search import search_files
from app.file_sender import send_file
from app.indexer import build_index, get_dashboard_info

app = FastAPI(title="JirasinOS")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup_event():
    build_index()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    dashboard = get_dashboard_info()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "dashboard": dashboard,
        },
    )


@app.get("/refresh")
def refresh():

    build_index()

    return RedirectResponse("/", status_code=303)


@app.get("/search", response_class=HTMLResponse)
def search(
    request: Request,
    keyword: str = "",
    message: str = "",
):

    results = search_files(keyword)

    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={
            "keyword": keyword,
            "results": results,
            "message": message,
        },
    )


@app.get("/send")
def send(path: str, keyword: str = ""):

    success, message = send_file(path)

    return RedirectResponse(
        url=f"/search?keyword={keyword}&message={message}",
        status_code=303,
    )


@app.get("/open-folder")
def open_folder(path: str, keyword: str = ""):

    folder = os.path.dirname(path)

    subprocess.Popen(
        [
            "explorer",
            folder,
        ]
    )

    return RedirectResponse(
        url=f"/search?keyword={keyword}",
        status_code=303,
    )


@app.get("/open-file")
def open_file(path: str, keyword: str = ""):

    os.startfile(path)

    return RedirectResponse(
        url=f"/search?keyword={keyword}",
        status_code=303,
    )