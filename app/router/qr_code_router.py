from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse

from schema.schemas import UrlData, WifiData, ContactData, GeoLocationData, EmailData, HealthCheck
from service.qr_code_service import url_to_qr_service, wifi_to_qr_service, contact_to_qr_service, geo_to_qr_service, email_to_qr_service


router = APIRouter()

@router.post("/url_to_qr")
async def url_to_qr(request: Request, 
                    info: UrlData) -> StreamingResponse:

    return await url_to_qr_service(request, info)


@router.post("/wifi_to_qr")
async def wifi_to_qr(request: Request, 
                     info: WifiData) -> StreamingResponse:

    return await wifi_to_qr_service(request, info)


@router.post("/contact_to_qr")
async def contact_to_qr(request: Request, 
                        info: ContactData) -> StreamingResponse:
    
    return await contact_to_qr_service(request, info)


@router.post("/geo_to_qr")
async def geo_to_qr(request: Request, 
                    info: GeoLocationData) -> StreamingResponse:
    
    return await geo_to_qr_service(request, info)


@router.post("/email_to_qr")
async def email_to_qr(request: Request, 
                      info: EmailData) -> StreamingResponse:
    
    return await email_to_qr_service(request, info)


@router.get("/health")
async def get_health() -> HealthCheck:

    return HealthCheck(status="OK")

# return templates.TemplateResponse("home.html", {"request": request, "qr_data": qr_data})