from fastapi import APIRouter, UploadFile, File
from PIL import Image
from pytesseract import image_to_string
from ocr.modules.credit_card import validate_credit_card
from ocr.modules.date import extract_dates_async
from ocr.modules.email import extract_emails_async
from ocr.modules.hash import extract_hashes_async
from ocr.modules.id import extract_id_numbers_async
from ocr.modules.phone_num import extract_phone_numbers_async
from ocr.modules.plate import extract_license_plates_async
from ocr.modules.url import extract_urls_async
import asyncio

router = APIRouter(
    prefix="/api/v1",
    tags=["ocr"],
    responses={404: {"description": "Not found"}},
)

async def perform_ocr(image):
    return image_to_string(image)

async def extract_sensitive_data(text):
    tasks = [
        validate_credit_card(text),
        extract_dates_async(text),
        extract_emails_async(text),
        extract_hashes_async(text),
        extract_id_numbers_async(text, "TR"),
        extract_phone_numbers_async(text),
        extract_license_plates_async(text),
        extract_urls_async(text)
    ]
    return await asyncio.gather(*tasks)

async def process_image_async(file):
    try:
        # Open image and use OCR
        image = Image.open(file.file)
        text = await perform_ocr(image)

        # if message is empty, return 204
        if not text.strip():
            return {"status": "No Content"}, 204

        extracted_sensitive_data = await extract_sensitive_data(text)

        response_data = {
            "status": "Successful",
            "text": text,
            "extracted_sensitive_data": {
                "credit_card": extracted_sensitive_data[0],
                "dates": extracted_sensitive_data[1],
                "emails": extracted_sensitive_data[2],
                "hashes": extracted_sensitive_data[3],
                "id_numbers": extracted_sensitive_data[4],
                "phone_numbers": extracted_sensitive_data[5],
                "license_plates": extracted_sensitive_data[6],
                "urls": extracted_sensitive_data[7]
            }
        }

        return response_data, 200

    except Exception as e:
        return {"status": "Bad Request", "message": str(e)}, 400

@router.post("/image/")
async def process_image_api(file: UploadFile = File(...)):
    return await process_image_async(file)
