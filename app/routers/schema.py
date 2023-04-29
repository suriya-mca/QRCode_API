from pydantic import BaseModel, HttpUrl
from datetime import date

# url to qr parameter schema
class UrlData(BaseModel):
    url: str

# wifi data to qr parameter schema
class WifiData(BaseModel):
    wifi_name: str
    wifi_password: str

# social links
class SocialLinks(BaseModel):
    linkedin_link: HttpUrl = None
    github_link: HttpUrl = None
    portfolio_website: HttpUrl = None

# work experience
class WorkExperience(BaseModel):
    experience_type: str
    position: str
    company_name: str
    start_date: date
    end_date: date = None
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
    social_links: list[SocialLinks]
    experience: list[WorkExperience] = None
    education: list[Course]
    certification: list[Certificate] = None



# code: bytes = pyqrcode.create(data) # convert data to QR(byte)
# qr_data: str = code.png_as_base64_str(scale=5) # convert byte code data to base64 string