from pydantic import BaseModel


class UrlData(BaseModel):
    url: str

class WifiData(BaseModel):
    wifi_name: str
    wifi_password: str

class ContactData(BaseModel):
    name: str
    email: str
    phone: str = None
    city: str
    org: str = None
    title: str = None
    url: str = None

class GeoLocationData(BaseModel):
    latitude: float
    longitude: float

class EmailData(BaseModel):
    to: str
    subject: str
    body: str
    cc: str = None