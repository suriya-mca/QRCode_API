from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import segno
import json
from segno import helpers
from .schema import UrlData, WifiData, ResumeData, CustomEncoder, ContactDetail

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


# Resume to OR code generator function
@router.post("/api/resume_to_qr")
async def resume_to_qr_generator(request: Request, info: ResumeData) -> HTMLResponse:

    data: dict = {
        "name": info.name,
        "email": info.email,
        "mobile": info.mobile,
        "country": info.country,
        "state": info.state,
        "city": info.city,
        "pincode": info.pincode,
        "social_links": {
            "linkedin_link": info.social_links.linkedin_link,
            "github_link": info.social_links.github_link,
            "portfolio_website": info.social_links.portfolio_website
        },
        "experience": info.experience,
        "education": info.education,
        "certification": info.certification
    }

    # convert data to QR(byte)
    qr_data: bytes = segno.make(json.dumps(data, cls=CustomEncoder).encode("utf-8"), error='H')
    return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Contact details to QR code generator function
@router.post("/api/contact_to_qr")
async def contact_to_qr_generator(request: Request, info: ContactDetail) -> HTMLResponse:
    
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

