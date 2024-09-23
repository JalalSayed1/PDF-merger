from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas

def svg_to_pdf(svg_files, output_pdf, preserve_dimensions=True):
    """
    Converts SVG images to a single PDF, preserving color profiles and dimensions.

    Args:
        svg_files: List of SVG file paths.
        output_pdf: Output PDF file path.
        preserve_dimensions: If True, keep original SVG dimensions in the PDF.
    """

    c = canvas.Canvas(output_pdf)

    for svg_file in svg_files:
        drawing = svg2rlg(svg_file)

        if preserve_dimensions:
            # Get original SVG dimensions
            width = drawing.width
            height = drawing.height

            # Set PDF page size to match SVG dimensions
            c.setPageSize((width, height))

        renderPDF.draw(drawing, c, 0, 0)
        c.showPage()

    c.save()

# Example usage
svg_files = ["Business Card - EN.svg", "Business Card - AR.svg"]
output_pdf = "combined.pdf"

svg_to_pdf(svg_files, output_pdf)