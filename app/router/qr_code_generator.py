from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import segno
from segno import helpers

from schema.schemas import UrlData, WifiData, ContactData, GeoLocationData, EmailData


router = APIRouter()

templates = Jinja2Templates(directory="templates")

# URL to QR code generator function
@router.post("/url_to_qr")
async def url_to_qr_generator(request: Request, info: UrlData) -> HTMLResponse:

    data: str = info.url
    qr_data: bytes = segno.make_qr(data, error = 'H') 
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Wifi Data to QR code generator function
@router.post("/wifi_to_qr")
async def wifi_to_qr_generator(request: Request, info: WifiData) -> HTMLResponse:

    name: str = info.wifi_name
    password: str = info.wifi_password
    data: bytes = helpers.make_wifi_data(ssid=name, password=password, security='WPA')
    qr_data: bytes = segno.make(data, error = 'H')
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Contact details to QR code generator function
@router.post("/contact_to_qr")
async def contact_to_qr_generator(request: Request, info: ContactData) -> HTMLResponse:
    
    data: bytes = helpers.make_vcard_data(
        displayname = info.name,
        name = info.name,
        email = info.email,
        phone = info.phone,
        city = info.city,
        org = info.org,
        title = info.title,
        url = info.url
    )
    qr_data: bytes = segno.make(data, error = 'H')
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Geographic location to QR code generator function
@router.post("/geo_to_qr")
async def geo_to_qr_generator(request: Request, info: GeoLocationData) -> HTMLResponse:
    
    data: bytes = helpers.make_geo_data(info.latitude, info.longitude)
    qr_data: bytes = segno.make(data, error = 'H')
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Email to QR QR code generator function
@router.post("/email_to_qr")
async def email_to_qr_generator(request: Request, info: EmailData) -> HTMLResponse:
    
    qr_data: bytes = helpers.make_email(
        to = info.to,
        subject = info.subject,
        body = info.body,
        cc = info.cc
    )
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})