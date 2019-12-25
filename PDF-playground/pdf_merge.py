import PyPDF2
import sys

# python pdf.py dummy.pdf twopage.pdf
inputs = sys.argv[1:]
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)

    with open('wtr.pdf', 'rb') as wtr_file:
        merger.merge(1, wtr_file)

    merger.write('super.pdf')

pdf_combiner(inputs)



# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
#     page1 = reader.getPage(0)
#     page1.rotateCounterClockwise(90)

#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page1)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)
