from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from app.pdf_generator import html_to_pdf
import os
import uuid

app = FastAPI()

GENERATED_DIR = "generated"
os.makedirs(GENERATED_DIR, exist_ok=True)

@app.post("/generate_pdf")
async def generate_pdf(html: str = Form(...)):
    file_id = str(uuid.uuid4())
    file_path = f"{GENERATED_DIR}/{file_id}.pdf"
    html_to_pdf(html, file_path)
    return JSONResponse(content={
        "download_url": f"http://44.222.249.128:8082/download/{file_id}.pdf"
    })

from fastapi.responses import FileResponse

@app.get("/download/{file_name}")
async def download_pdf(file_name: str):
    file_path = os.path.join(GENERATED_DIR, file_name)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/pdf", filename=file_name)
    return JSONResponse(content={"error": "Arquivo não encontrado"}, status_code=404)
