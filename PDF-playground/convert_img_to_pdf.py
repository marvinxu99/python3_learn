from PIL import Image

def convert_image_to_pdf(image_path, pdf_path):
    # Open the image
    image = Image.open(image_path)

    # Convert to RGB mode if the image has an alpha channel
    if image.mode in ("RGBA", "P"):
        image = image.convert("RGB")

    # Save as PDF
    image.save(pdf_path, "PDF")
    print(f"PDF saved to: {pdf_path}")

# Example usage
# convert_image_to_pdf("example.jpg", "output.pdf")
