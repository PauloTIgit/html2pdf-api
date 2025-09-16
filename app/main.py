from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import StreamingResponse
from app.pdf_generator import html_to_pdf
from io import BytesIO

app = FastAPI(title="HTML to PDF API")

@app.post("/generate-pdf/")
async def generate_pdf(html: str = Form(...), file: str = 'saida'):
    """
    Recebe HTML via form-data e retorna PDF
    """
    pdf_bytes = html_to_pdf(html)
    return StreamingResponse(BytesIO(pdf_bytes), media_type="application/pdf", headers={
        'Content-Disposition': 'attachment; filename='+file+'.pdf'
    })

@app.get("/")
async def root():
    return {"message": "HTML to PDF API funcionando!"}
