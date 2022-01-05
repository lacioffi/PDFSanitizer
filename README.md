# PDFSanitizer
Renders possibly malicious PDF files and outputs harmless PDF files  

To do this, the PDF files are rendered and converted to images using PyMuPDF.
The images are then saved to a new PDF file using img2pdf. This ensures no visual data is lost,
but any scripts/external references/flash files are removed.

<b>Instalation</b>: pip install -r requirements.txt <br>
<b>Usage</b>: pdfsanitizer.py <filename> <output folder>

This project uses the following libraries:
    
    PyMuPDF - By Jorj X. McKie (@JorjMcKie)
    
    img2pdf - By Johannes Schauer Marin Rodrigues (josch@mister-muffin.de)

This script will render possibly malicious PDFs to generate the sanitized file, so it should always run
on a sandbox, an isolated ephemeral instance or similar. Assume the machine this runs on will be pwned eventually. 
  
### To-do
This method removes EVERYTHING from the PDF. It would be nice to at least keep the text copy-pasteable.
