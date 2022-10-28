from pdf2docx import parse

pdf_file = './main.pdf'
docx_file = './main.docx'

# convert pdf to docx
parse(pdf_file, docx_file)