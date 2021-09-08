# Required Module:- pip install PyPDF2

from PyPDF2 import PdfFileMerger

pdfs = ["Pdf_1.pdf", "Pdf_2.pdf"]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("Final_Pdf.pdf")

merger.close()