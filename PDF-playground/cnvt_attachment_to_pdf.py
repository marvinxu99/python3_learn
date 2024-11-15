import os
from PIL import Image  # For image conversion  (Pillow)
from docx import Document  # For Word document conversion (python-docx)
from fpdf import FPDF  # For generating PDFs   (fpdf)

# openpyxl  for *.xls
# python-pptx for *.pptx

def convert_image_to_pdf(image_path, pdf_path):
    """Convert an image to a PDF."""
    image = Image.open(image_path)
    if image.mode in ("RGBA", "P"):  # Convert image to RGB if it has transparency
        image = image.convert("RGB")
    image.save(pdf_path, "PDF")

def convert_docx_to_pdf(docx_path, pdf_path):
    """Convert a Word document to a PDF (simple text extraction)."""
    document = Document(docx_path)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add content from Word document to the PDF
    for paragraph in document.paragraphs:
        pdf.multi_cell(0, 10, paragraph.text)

    pdf.output(pdf_path)

def process_attachment(attachment, save_dir):
    """Process an attachment and save or convert it to PDF."""
    file_path = os.path.join(save_dir, attachment.FileName)
    attachment.SaveAsFile(file_path)  # Save the original file
    print(f"Saved attachment: {file_path}")

    # Determine the file type and convert to PDF if needed
    if file_path.endswith((".jpg", ".png")):
        pdf_path = file_path.rsplit(".", 1)[0] + ".pdf"
        convert_image_to_pdf(file_path, pdf_path)
        print(f"Converted image to PDF: {pdf_path}")

    elif file_path.endswith(".docx"):
        pdf_path = file_path.rsplit(".", 1)[0] + ".pdf"
        convert_docx_to_pdf(file_path, pdf_path)
        print(f"Converted Word document to PDF: {pdf_path}")

    # Add other file type conversions as needed...
