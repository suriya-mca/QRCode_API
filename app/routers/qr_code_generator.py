from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import segno
from segno import helpers
from .schema import UrlData, WifiData, ResumeData

# router instance
router = APIRouter()

# template directory
templates = Jinja2Templates(directory="templates")

# URL to QR code generator function
@router.post("/api/url_to_qr")
async def url_to_qr_generator(request: Request, info: UrlData) -> HTMLResponse:

    data: str = info.url

    # convert data to QR(byte)
    qr_data: bytes = segno.make_qr(data) 
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Wifi Data to QR code generator function
@router.post("/api/wifi_to_qr")
async def wifi_to_qr_generator(request: Request, info: WifiData) -> HTMLResponse:

    name: str = info.wifi_name
    password: str = info.wifi_password

    # convert data to QR(byte)
    qr_data: bytes = helpers.make_wifi(ssid=name, password=password, security='WPA')
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Resume to OR code generator function
@router.post("/api/resume_to_qr")
async def resume_to_qr_generator(request: Request, info: ResumeData) -> HTMLResponse:
    
    return info