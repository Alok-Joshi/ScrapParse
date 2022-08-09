from PyPDF2 import PdfReader



def pdf_to_text(pdf_name):
    """ Converts the pdf into a text string """

    reader = PdfReader("cl_1.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text()+"\n"
    
    return text

def get_date(case_number,text):
    """ Extracts the date for the given case_number """ 
    pass



