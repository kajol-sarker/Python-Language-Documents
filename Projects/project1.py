from PyPDF2 import PdfMerger
allpdf = ['1.pdf', '2.pdf']
merger = PdfMerger()

for newpdf in allpdf:
    merger.append(newpdf)

merger.write("Updated.pdf")
merger.close()