from PyPDF2 import PdfReader
import docx
import os

def extract_text_from_file(file_path):
    # Detect file type by extension (try to preserve original extension)
    ext = os.path.splitext(file_path)[-1].lower()
    text = ""

    try:
        # Handle PDF
        if ext == ".pdf" or "pdf" in file_path.lower():
            reader = PdfReader(file_path)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

        # Handle DOCX
        elif ext == ".docx" or "docx" in file_path.lower():
            doc = docx.Document(file_path)
            text = "\n".join([p.text for p in doc.paragraphs])

        # Handle plain text
        else:
            # Try multiple encodings to avoid UnicodeDecodeError
            for encoding in ["utf-8", "latin-1", "ISO-8859-1"]:
                try:
                    with open(file_path, "r", encoding=encoding, errors="ignore") as f:
                        text = f.read()
                        break
                except Exception:
                    continue

    except Exception as e:
        text = f"Error reading file: {e}"

    return text.strip() or "No readable text found in the file."
