from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pyqrcode
from .schema import Data

# router instance
router = APIRouter()

# template directory
templates = Jinja2Templates(directory="templates")

# QR code generator function
@router.post("/api/qr")
def qr_generator(request: Request, info: Data):

    data = info.url

    code = pyqrcode.create(data)
    qr_data = code.png_as_base64_str(scale=5)

    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})