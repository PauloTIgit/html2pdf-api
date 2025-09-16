from weasyprint import HTML
from io import BytesIO

def html_to_pdf(html_content: str) -> bytes:
    """
    Recebe HTML e retorna PDF em bytes
    """
    pdf_bytes = BytesIO()
    HTML(string=html_content).write_pdf(target=pdf_bytes)
    pdf_bytes.seek(0)
    return pdf_bytes.read()
