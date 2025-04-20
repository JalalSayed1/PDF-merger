# PDF-MERGER

A lightweight Python toolset for merging PDF files.

## Table of Contents

- [PDF-MERGER](#pdf-merger)
  - [Table of Contents](#table-of-contents)
  - [Requirements](#requirements)
  - [PDF\_merger\_all.py](#pdf_merger_allpy)
    - [How It Works](#how-it-works)
    - [Usage](#usage)
    - [Output](#output)
  - [PDF\_merger.py](#pdf_mergerpy)
    - [Usage](#usage-1)
    - [Output](#output-1)
  - [svg\_to\_pdf.py](#svg_to_pdfpy)
    - [Example Usage](#example-usage)
  - [License](#license)
  - [Contributions](#contributions)

## Requirements

Install the required libraries:

```bash
pip install PyPDF2 svglib reportlab
```

## PDF_merger_all.py

This script merges **all PDF files** located in the `pdfs_to_merge/` folder.

### How It Works

- Scans the `pdfs_to_merge/` directory.
- Filters `.pdf` files.
- Merges all files alphabetically into `merged_output.pdf`.

### Usage

```bash
python PDF_merger_all.py
```

### Output

Creates a new file named `merged_output.pdf` in the current working directory.

## PDF_merger.py

Merge two specified PDF files into one. It expects both files to be present in the **current working directory**.

### Usage

```bash
python PDF_merger.py file1.pdf file2.pdf
```

### Output

Creates a new file named `merged.pdf` in the current working directory.

## svg_to_pdf.py

Converts one or more SVG images into a single PDF file, preserving dimensions and colours.

### Usage

Edit the python script to specify the SVG files you want to convert and the output PDF file name:

```python
svg_files = ["Business Card - EN.svg", "Business Card - AR.svg"]
output_pdf = "combined.pdf"

svg_to_pdf(svg_files, output_pdf)
```

## License

This project is licensed under the [Creative Commons Zero v1.0 Universal (CC0)](https://creativecommons.org/publicdomain/zero/1.0/) licence. 

You are free to use, modify, and distribute the code without any restrictions or the need for attribution.

## Contributions

Pull requests and feedback welcome. Please fork the repo and submit a PR.
