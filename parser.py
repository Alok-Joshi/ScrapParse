from PyPDF2 import PdfReader
import re
import logging

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

def create_table(text):
    """ Creates the hash table with (key : value), with key as the table(string) which comes under the CASES AT SR.. Line, and the value as its corresponding date """

    text_lines = text.split("\n")
    table = dict()
    case_line_positions = []

    for i in range(len(text_lines)):
        if(re.search("CASES AT",text_lines[i])): #use regex here later 
            case_line_positions.append(i)
            
    case_line_positions.append(len(text_lines) - 1) #for the last part
    logging.info("Case Line Numbers: "+str(case_line_positions))

    for i in range(len(case_line_positions)-1):
        lower_pos = case_line_positions[i] #the date
        upper_pos = case_line_positions[i+1] #The next date,but just before 
        key = ""
        for j in range(lower_pos+1, upper_pos):
            key += text_lines[j]

        table[key] = extract_date(text_lines[lower_pos])

    return table

def get_date(case_number,table):
    """ Extracts the date for the given case_number """ 
    
    for content in table:
        if(re.search(case_number ,content)):
            return table[content]

    return None
def generate_regex_string(string):
    """ Converts the string into a regex appropriate format 
        "116/2017(WZ)" --> "116/2017\(WZ\)  ( '(' is a special character for regex and hence to make sure it matches and its special meaning is not used we add a \ before it 
        """
    pass
    regex_string = ""
    for char in string:
        if(char == '(' or char == ')'):
            regex_string += "\\"

        regex_string += char
    return regex_string



