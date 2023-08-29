from fastapi import APIRouter
from ocr.api.v1.endpoint import deneme

router = APIRouter()
router.include_router(deneme.router)