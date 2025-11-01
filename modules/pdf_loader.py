import fitz 

# extracting text from the given pdf
def extract_text_from_pdf (pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text = text + page.get_text()
    
    return text