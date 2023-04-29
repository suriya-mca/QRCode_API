from pydantic import BaseModel

# url to qr parameter schema
class UrlData(BaseModel):
    url: str

# wifi data to qr parameter schema
class WifiData(BaseModel):
    wifi_name: str
    wifi_password: str




# code: bytes = pyqrcode.create(data) # convert data to QR(byte)
# qr_data: str = code.png_as_base64_str(scale=5) # convert byte code data to base64 string