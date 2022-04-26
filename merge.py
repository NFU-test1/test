from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
path = r'C:/Users/40741409/Desktop/pdf'
pdf_writer = PdfFileWriter()

#for i in range(1, 6):
    #pdf_reader = PdfFileReader(path + '/INV1-{}.pdf'.format(i))

for file in glob.glob(r'C:/Users/40741409/Desktop/pdf/*.pdf'):
    pdf_reader = PdfFileReader(file)
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
    
with open('C:/Users/40741409/Desktop/test' + r'/mergePDF/merge.pdf', 'wb') as out:
    pdf_writer.write(out)