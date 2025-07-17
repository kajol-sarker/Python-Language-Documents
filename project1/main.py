
from PyPDF2 import PdfMerger
allpdf = ["E:\My Project\\Python Language\\project1\\1.pdf", "E:\\My Project\\Python Language\\project1\\2.pdf"]
merger = PdfMerger()

for newpdf in allpdf:
    merger.append(newpdf)

merger.write("Updated.pdf")
merger.close()