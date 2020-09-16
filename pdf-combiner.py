import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
       print(pdf)
       merger.append(pdf)
    merger.write('new_pdf.pdf')

pdf_combiner(inputs)

def pdf_watermark(watermark, pdf_list):