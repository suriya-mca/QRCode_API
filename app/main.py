from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse

from router import qr_code_router


app = FastAPI(default_response_class=UJSONResponse)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["application/json"],
)

app.include_router(
    qr_code_router.router,
    prefix="/api/v1"
)