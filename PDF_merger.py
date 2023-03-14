import PyPDF2
import os
import sys

# get the name of both pdf files from cmd line:

file1 = sys.argv[1]
file2 = sys.argv[2]

# check if the files exist:
# get the current working directory:
cwd = os.getcwd()

for file in [file1, file2]:
    
    # check if both files are pdfs:
    if not file.endswith('.pdf'):
        print(f'The file {file} is not a pdf file')
        # convert the file to pdf:
        # TODO convert the file to pdf
        sys.exit()
    
    if not os.path.exists(file):
        print(f'The file {file} does not exist in the current working directory {cwd}')
        sys.exit()

# merge the two pdf files:
pdf1 = PyPDF2.PdfReader(file1)
pdf2 = PyPDF2.PdfReader(file2)
pdf3 = PyPDF2.PdfWriter()
for page in range(len(pdf1.pages)):
    pdf3.add_page(pdf1.pages[page])
    
for page in range(len(pdf2.pages)):
    pdf3.add_page(pdf2.pages[page])

# save the merged pdf file:
with open('merged.pdf', 'wb') as f:
    pdf3.write(f)

