from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

api_router = APIRouter()


@api_router.get("/preview", response_class=HTMLResponse)
async def preview_template(request: Request):
    content = "Hello, world!"
    return templates.TemplateResponse("email_templates/preview.html", {"request": request, "content": content})
