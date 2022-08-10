from PyPDF2 import PdfReader
import re


def pdf_to_text(pdf_name):
    """ Converts the pdf into a text string """

    reader = PdfReader(pdf_name)
    text = ""
    for page in reader.pages:
        text += page.extract_text()+"\n"
    
    return text
def extract_date(date_string):
    """ Takes the "CASES AT SR ... ON 02.08.2022" string and returns the date from it (in string format //can be changed ) """

    date_string = date_string.split() #Last element gives us the date 
    date = date_string[len(date_string)-1]
    return date

def get_case_date_htable(text):
    """ Creates the hash table with (key : value), with key as the table(string) which comes under the CASES AT SR.. Line, and the value as its corresponding date """

    text_lines = text.split("\n")
    table = dict()
    case_line_positions = []

    for i in range(len(text_lines)):
        if("CASES AT" in text_lines[i]): #use regex here later 
            case_line_positions.append(i)
            
    case_line_positions.append(len(text_lines) - 1) #for the last part
    print(case_line_positions)
    for i in range(len(case_line_positions)-1):
        lower_pos = case_line_positions[i] #the date
        upper_pos = case_line_positions[i+1] #The next date,but just before 
        key = ""
        for j in range(lower_pos+1, upper_pos):
            key += text_lines[j]

        table[key] = extract_date(text_lines[lower_pos])

    return table



def get_date(case_number,text):
    """ Extracts the date for the given case_number """ 
    


