import pytesseract
from pdf2image import convert_from_path
import glob
import re
import options
import sqlite3
import SQL
#pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

def generate_extract(pdfPath):
    pdfs = glob.glob(pdfPath)

    for pdf_path in pdfs:
        pages = convert_from_path(pdf_path, 500)
        page_contents = []
        for imgBlob in pages:
            page_contents.append(pytesseract.image_to_string(imgBlob,lang='eng'))
    return page_contents

def unique_words(text):
    word_list = []
    for word in text:
        if word.upper() not in word_list and len(word) > options.MINIMUM_WORD_LENGTH:
            word_list.append(word.upper())
    return word_list

def extract_text(text):
    return unique_words(re.findall(r'\b[a-zA-Z]+\b', text))

def compare_to_wordList(page, word_list):
    match = {}
    for folder in word_list:
        comp = set(page).intersection(word_list[folder])
        match[folder] = len(comp)
        print("Page has " + str(round(len(comp) / len(page), 3)) + "% similarity to " + folder)
    
    return match


def main():
    con = sqlite3.connect("mailSort.db")
    cur = con.cursor()

    word_list = SQL.get_words(cur)
    for page in generate_extract('example.pdf'):
        print(compare_to_wordList(extract_text(page),word_list))

    

if __name__ == "__main__":
    main()