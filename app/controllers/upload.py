from fastapi import APIRouter, UploadFile, File, BackgroundTasks
from app.services.process import process_bill

router = APIRouter()

@router.post("/")
async def upload(background_tasks: BackgroundTasks, data: UploadFile = File(...)):
    ret = process_bill(data)
    background_tasks.add_task(data.file.close)
    return ret
