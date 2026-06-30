from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import UploadFile
from sqlmodel import Session

from database.database import get_session
from schemas.response import APIResponse
from services.upload_service import UploadService

router = APIRouter()


@router.post("/")
async def upload_document(
    file: UploadFile = File(...),
    session: Session = Depends(get_session),
):

    document = await UploadService.upload(
        file,
        session,
    )

    return APIResponse(
        success=True,
        message="Upload successful.",
        data=document,
    )