from fastapi import APIRouter, Request
import io
from fastapi.responses import StreamingResponse
import segno
from segno import helpers

from schema.schemas import UrlData, WifiData, ContactData, GeoLocationData, EmailData


router = APIRouter()

# URL to QR code generator function
@router.post("/url_to_qr")
async def url_to_qr_generator(request: Request, info: UrlData) -> StreamingResponse:

    data: str = info.url
    qr_data: bytes = segno.make_qr(data, error = 'H')
    qr_buffer = io.BytesIO()
    qr_data.save(qr_buffer, kind='png', scale=10)
    qr_buffer.seek(0)
    return StreamingResponse(content=qr_buffer, media_type="image/png")
    # return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})


# Wifi Data to QR code generator function
@router.post("/wifi_to_qr")
async def wifi_to_qr_generator(request: Request, info: WifiData) -> StreamingResponse:

    name: str = info.wifi_name
    password: str = info.wifi_password
    data: bytes = helpers.make_wifi_data(ssid=name, password=password, security='WPA')
    qr_data: bytes = segno.make(data, error = 'H')
    qr_buffer = io.BytesIO()
    qr_data.save(qr_buffer, kind='png', scale=10)
    qr_buffer.seek(0)
    return StreamingResponse(content=qr_buffer, media_type="image/png")


# Contact details to QR code generator function
@router.post("/contact_to_qr")
async def contact_to_qr_generator(request: Request, info: ContactData) -> StreamingResponse:
    
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
    qr_buffer = io.BytesIO()
    qr_data.save(qr_buffer, kind='png', scale=10)
    qr_buffer.seek(0)
    return StreamingResponse(content=qr_buffer, media_type="image/png")


# Geographic location to QR code generator function
@router.post("/geo_to_qr")
async def geo_to_qr_generator(request: Request, info: GeoLocationData) -> StreamingResponse:
    
    data: bytes = helpers.make_geo_data(info.latitude, info.longitude)
    qr_data: bytes = segno.make(data, error = 'H')
    qr_buffer = io.BytesIO()
    qr_data.save(qr_buffer, kind='png', scale=10)
    qr_buffer.seek(0)
    return StreamingResponse(content=qr_buffer, media_type="image/png")


# Email to QR QR code generator function
@router.post("/email_to_qr")
async def email_to_qr_generator(request: Request, info: EmailData) -> StreamingResponse:
    
    qr_data: bytes = helpers.make_email(
        to = info.to,
        subject = info.subject,
        body = info.body,
        cc = info.cc
    )
    qr_buffer = io.BytesIO()
    qr_data.save(qr_buffer, kind='png', scale=10)
    qr_buffer.seek(0)
    return StreamingResponse(content=qr_buffer, media_type="image/png")