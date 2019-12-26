import PyPDF2
import sys

# add water mark
template = PyPDF2.PdfFileReader(open('twopage.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open("watermarked_output.pdf", 'wb') as file:
    output.write(file)


# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page1 = reader.getPage(0)
#     page1.rotateCounterClockwise(90)

#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page1)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
