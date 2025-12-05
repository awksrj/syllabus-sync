from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/upload")
def upload_form(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})
