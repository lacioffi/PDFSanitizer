#!/usr/bin/env python

__description__ = 'Tool to sanitize PDF files'
__author__ = 'Lucas Andrade Cioffi'
__version__ = '1.0.0'
__date__ = '2022/01/05'

"""
Tool to generate sanitized versions of PDF files.

To do this, the PDF files are rendered and converted to images using PyMuPDF.
The images are then saved to a new PDF file using P. This ensures no visual data is lost,
but any scripts/external references/flash files are removed.

Instalation: pip install -r requirements.txt
Usage: pdfsanitizer.py <filename> <output folder>

This project uses the following libraries:
    PyMuPDF - By Jorj X. McKie (@JorjMcKie)
    img2pdf - By Johannes Schauer Marin Rodrigues (josch@mister-muffin.de)

This script will render malicious PDFs to generate the sanitized file, so it should always run
on a sandbox, an isolated ephemeral instance or similar. Assume the machine this runs on will be pwned. 
""" 


#####################################################################
import sys
import fitz
import img2pdf
from pathlib import Path

filename = ""
try:
    filename = sys.argv[1]
except:
    print("No file specified!")
    print("Usage: pdfsanitizer.py <filename> <output folder>")
    exit()  

outputFolder = ""
try:
    outputFolder = sys.argv[2]
    if(Path(outputFolder).exists() and (not Path(outputFolder).is_dir())):
        exit()
    elif (not Path(outputFolder).exists()):
        print("Output directory not found, creating...")
        Path(outputFolder).mkdir(parents=True, exist_ok=True)
except:
    print("Please specify a valid directory as output!")
    print("Usage: pdfsanitizer.py <filename> <output folder>")
    exit()  

# Render and convert to images

try:
    doc = fitz.open(filename)
    print("File opened...")
except:
    print("Invalid filename!")
    exit()
images = []
for i in range(0, doc.page_count):
    page = doc.load_page(i) 
    images.append(page.get_pixmap(matrix=fitz.Matrix(150/72,150/72)).tobytes())
    print("Rendered page " + str(i+1) + " out of " + str(doc.page_count) + " pages...")

# Save to PDF file
try:
    with open(outputFolder+"/"+filename, "wb") as f:
        f.write(img2pdf.convert(images))
        print("Sanitized PDF saved successfully at " + outputFolder+"/"+filename)
except:
    print("Something went wrong while saving the file. Did you specify a valid file?")

