from pydantic import BaseModel, HttpUrl
from datetime import date
import json
from json import JSONEncoder

# url to qr parameter schema
class UrlData(BaseModel):
    url: HttpUrl

# wifi data to qr parameter schema
class WifiData(BaseModel):
    wifi_name: str
    wifi_password: str

# custom encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, o):
            return o.__dict__

# contact details to qr parameter schema
class ContactDetail(BaseModel):
    name: str
    email: str
    phone: str = None
    city: str
    org: str = None
    title: str = None
    url: HttpUrl = None

# geographic location to qr parameter schema
class GeoLocation(BaseModel):
    latitude: float
    longitude: float

# code: bytes = pyqrcode.create(data) # convert data to QR(byte)
# qr_data: str = code.png_as_base64_str(scale=5) # convert byte code data to base64 string
# data: str = helpers.make_mecard_data(info)