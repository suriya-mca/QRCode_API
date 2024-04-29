# QR Code Generator API

API to generate dynamic QR code for URL / Link, facilitating wifi authentication, sharing contact details, sharing geographic location and email communication.

## Endpoints

- `POST /url_to_qr`: Generate QR code for a URL.
- `POST /wifi_to_qr`: Generate QR code for WiFi credentials.
- `POST /contact_to_qr`: Generate QR code for contact information.
- `POST /geo_to_qr`: Generate QR code for geographic location.
- `POST /email_to_qr`: Generate QR code for an email.

### Payloads Schema

#### /url_to_qr
```json
{
    "url": "string"
}
```

#### /wifi_to_qr
```json
{
    "wifi_name": "string",
    "wifi_password": "string"
}
```

#### /contact_to_qr
```json
{
    "name": "string",
    "email": "string",
    "phone": "string",
    "city": "string",
    "org": "string",
    "title": "string",
    "url": "string"
}
```

#### /geo_to_qr
```json
{
    "latitude": 0,
    "longitude": 0
}
```

#### /email_to_qr
```json
{
    "to": "string",
    "subject": "string",
    "body": "string",
    "cc": "string"
}
```