import PyPDF2 
import os

def merge_pdf(input_folder, output_file):
    pdf2merge = []
    for filename in os.listdir(input_folder):
        #print(filename)
        if filename.endswith('.pdf'):
            pdf2merge.append(filename)
    pdf2merge.sort()
    
    pdfWriter = PyPDF2.PdfFileWriter()
    for filename in pdf2merge:
        pdfFileObj = open(input_folder+"/"+filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        for pageNum in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)
            
    pdfOutput = open(output_file+'.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    #Outputting the PDF
    pdfOutput.close()

merge_pdf('C:/Users/40741409/Desktop/pdf','inv2')