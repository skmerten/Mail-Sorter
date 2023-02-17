import pytesseract
from pdf2image import convert_from_path
import glob
import re
import options
import sqlite3
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

def main():
    for page in generate_extract('example.pdf'):
        print(extract_text(page))


if __name__ == "__main__":
    main()