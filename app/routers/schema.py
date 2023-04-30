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

# social links
class SocialLinks(BaseModel):
    linkedin: HttpUrl = None
    github: HttpUrl = None
    portfolio_website: HttpUrl = None

# work experience
class WorkExperience(BaseModel):
    experience_type: str
    position: str
    company_name: str
    start_date: str
    end_date: str = None
    description: str = None

# course details
class Course(BaseModel):
    degree_type: str
    fulltime_or_parttime: str
    degree: str
    major: str
    college_name: str
    college_country: str
    college_state: str
    college_city: str
    year_of_completion: int
    cgpa: int
    status: str 

# certifications
class Certificate(BaseModel):
    certificate_name: str
    institute: str
    certificate_link: HttpUrl = None

# resume data to qr parameter schema
class ResumeData(BaseModel):
    name: str
    email: str
    mobile: str = None
    country: str
    state: str
    city: str
    pincode: int
    social_links: SocialLinks
    experience: list[WorkExperience] = None
    education: list[Course]
    certification: list[Certificate] = None

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



# code: bytes = pyqrcode.create(data) # convert data to QR(byte)
# qr_data: str = code.png_as_base64_str(scale=5) # convert byte code data to base64 string
# data: str = helpers.make_mecard_data(info)