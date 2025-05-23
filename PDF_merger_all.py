import PyPDF2
import os

# Get the current working directory
cwd = os.getcwd()
pdf_folder = os.path.join(cwd, 'pdfs_to_merge')

# List all files in the current directory
files = os.listdir(pdf_folder)

# Filter out only PDF files
pdf_files = [file for file in files if file.endswith('.pdf')]

print(f"Found {len(pdf_files)} PDF files in the directory:")
for pdf_file in pdf_files:
    print(f" - {pdf_file}")

# Check if there are at least two PDFs to merge
if len(pdf_files) < 2:
    print("There are not enough PDF files in the current directory to merge.")
    exit()

# Sort the PDF files alphabetically (optional, for predictable order)
pdf_files.sort()

# Create a PDF writer object to store the merged PDF
pdf_writer = PyPDF2.PdfWriter()

# Loop through each PDF file and add its pages to the writer
for pdf_file in pdf_files:
    print(f"Adding {pdf_file} to the merged PDF...")
    pdf_reader = PyPDF2.PdfReader(os.path.join(pdf_folder, pdf_file))
    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])

# Save the merged PDF file
output_file = 'merged_output.pdf'
with open(output_file, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

GREEN_BG = "\033[42m"
RESET = "\033[0m"
print(f"{GREEN_BG}Merged PDF created successfully as {output_file}.{RESET}")

