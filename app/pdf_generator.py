# pdf_generator.py
from weasyprint import HTML, CSS

def html_to_pdf(html: str) -> bytes:
    css = CSS(string='@page { size: A4; margin: 20mm; }')
    return HTML(string=html).write_pdf(stylesheets=[css])