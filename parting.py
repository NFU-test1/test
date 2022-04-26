from PyPDF2 import PdfFileReader, PdfFileWriter
path = r'C:\Users\40741409\Desktop\test'
pdf_reader = PdfFileReader(path + '\inv2.pdf')

for page in range(pdf_reader.getNumPages()):
    
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf_reader.getPage(page))
    with open(path + '\INV1-{}.pdf'.format(page + 1), 'wb') as out:
        pdf_writer.write(out)