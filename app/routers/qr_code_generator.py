from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import segno
import json
from segno import helpers
from .schema import UrlData, WifiData, CustomEncoder, ContactDetail, GeoLocation, Email

# router instance
router = APIRouter()

# template directory
templates = Jinja2Templates(directory="templates")

# URL to QR code generator function
@router.post("/api/url_to_qr")
async def url_to_qr_generator(request: Request, info: UrlData) -> HTMLResponse:

    data: HttpUrl = info.url

    # convert data to QR(byte)
    qr_data: bytes = segno.make_qr(data, error = 'H') 
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Wifi Data to QR code generator function
@router.post("/api/wifi_to_qr")
async def wifi_to_qr_generator(request: Request, info: WifiData) -> HTMLResponse:

    name: str = info.wifi_name
    password: str = info.wifi_password

    # convert data to QR(byte)
    data: bytes = helpers.make_wifi_data(ssid=name, password=password, security='WPA')
    qr_data: bytes = segno.make(data, error = 'H')
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Contact details to QR code generator function
@router.post("/api/contact_to_qr")
async def contact_to_qr_generator(request: Request, info: ContactDetail) -> HTMLResponse:
    
    # convert data to QR(byte)
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
@router.post("/api/geo_to_qr")
async def geo_to_qr_generator(request: Request, info: GeoLocation) -> HTMLResponse:
    
    # convert data to QR(byte)
    data: bytes = helpers.make_geo_data(info.latitude, info.longitude)
    qr_data: bytes = segno.make(data, error = 'H')
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Email to QR QR code generator function
@router.post("/api/email_to_qr")
async def email_to_qr_generator(request: Request, info: Email) -> HTMLResponse:
    
    # convert data to QR(byte)
    qr_data: bytes = helpers.make_email(
        to = info.to,
        subject = info.subject,
        body = info.body,
        cc = info.cc
    )
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})