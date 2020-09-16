from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

watermark_pdf = sys.argv[1]
input_pdf = sys.argv[2]

def pdf_watermark(watermark_pdf, input_pdf):
    watermark = PdfFileReader(watermark_pdf).getPage(0)

    pdf = PdfFileReader(input_pdf)
    writer = PdfFileWriter()

    for page in range(pdf.getNumPages()):
        pdf_page = pdf.getPage(page)
        pdf_page.mergePage(watermark)
        writer.addPage(pdf_page)

    with open(f'watermarked_{input_pdf}', 'wb') as new:
        writer.write(new)

pdf_watermark(watermark_pdf, input_pdf)