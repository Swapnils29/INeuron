from PyPDF2 import PdfFileMerger,PdfFileReader
import logging as logg

def merge(pdffiles):
    try:
        if len(pdffiles)>0:
            mergedObject = PdfFileMerger()
            for filepath in pdffiles:
                mergedObject.append(PdfFileReader(filepath, 'rb'))
            mergedObject.write("mergedfilesoutput.pdf")
    except Exception as er:
        raise er




