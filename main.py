import markdown
import weasyprint
import os

def generate_pdf():
    print("Initiating PDF conversion...")
    
    infile = "README.md"
    outfile = "Statistical_Analysis_of_Food_Delivery_Order_Demand.pdf"
    
    if not os.path.exists(infile):
        print(f"Error: {infile} not found.")
        return
        
    # Read the markdown report
    with open(infile, "r", encoding="utf-8") as f:
        md_text = f.read()
        
    # Convert Markdown to HTML utilizing table extensions and code blocks
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'codehilite'])
    
    # Professionally styled CSS optimized for A4 PDF generation
    css_string = """
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        line-height: 1.6;
        color: #333333;
        margin: 0;
    }
    h1, h2, h3, h4 {
        color: #1A365D;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
    }
    h1 { font-size: 24pt; border-bottom: 2px solid #1A365D; padding-bottom: 5px; }
    h2 { font-size: 18pt; border-bottom: 1px solid #E2E8F0; padding-bottom: 5px; }
    h3 { font-size: 14pt; }
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 1.5em auto;
        border: 1px solid #E2E8F0;
        border-radius: 4px;
        box-shadow: 0px 4px 6px -1px rgba(0,0,0,0.1), 0px 2px 4px -1px rgba(0,0,0,0.06);
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 1.5em 0;
        font-size: 11pt;
    }
    th, td {
        padding: 12px;
        text-align: left;
        border: 1px solid #CBD5E0;
    }
    th {
        background-color: #EDF2F7;
        font-weight: 600;
        color: #2D3748;
    }
    pre {
        background-color: #2D3748;
        color: #E2E8F0;
        padding: 15px;
        border-radius: 6px;
        font-family: 'Courier M', 'Courier New', monospace;
        font-size: 9pt;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    code {
        font-family: 'Courier M', 'Courier New', monospace;
        font-size: 10pt;
    }
    p {
        text-align: justify;
        text-justify: inter-word;
    }
    blockquote {
        border-left: 4px solid #A0AEC0;
        padding-left: 15px;
        color: #4A5568;
        font-style: italic;
        background-color: #F7FAFC;
        padding: 10px 15px;
        border-radius: 0 4px 4px 0;
    }
    a {
        color: #3182CE;
        text-decoration: none;
    }
    /* Strictly enforce Page Breaks */
    div[style*="page-break-after: always"], hr {
        page-break-after: always;
        visibility: hidden;
        height: 0;
    }
    /* Pagination and Page Margins */
    @page {
        size: A4;
        margin: 2cm 1.5cm;
        @bottom-right {
            content: "Page " counter(page) " of " counter(pages);
            font-size: 9pt;
            color: #718096;
            font-family: Helvetica, sans-serif;
        }
        @top-left {
            content: "Term Project Report";
            font-size: 8pt;
            color: #A0AEC0;
            font-family: Helvetica, sans-serif;
        }
    }
    """
    
    # Base structure container
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Term Project Final Report</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    print("Base HTML mapping compiled. Engaging WeasyPrint rendering engine...")
    
    base_url = os.path.abspath('.')
    
    # WeasyPrint export with inline styled CSS definitions
    html = weasyprint.HTML(string=full_html, base_url=base_url)
    css = weasyprint.CSS(string=css_string)
    
    html.write_pdf(outfile, stylesheets=[css])
    
    print(f"✓ Professional PDF successfully rendered as: {outfile}")

if __name__ == "__main__":
    generate_pdf()
