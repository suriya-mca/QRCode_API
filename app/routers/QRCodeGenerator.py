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
async def qr_generator(request: Request, info: Data) -> HTMLResponse:

    data: str = info.url

    code: bytes = pyqrcode.create(data) # convert data to QR(byte)
    qr_data: str = code.png_as_base64_str(scale=5) # convert byte code data to base64 string

    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})