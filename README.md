## **ASPX-Web-Scraper**

  This is a Python-based tool that scrapes **ASPX webpages** and converts them into **PDFs while preserving formatting**. This tool ensures that JavaScript-rendered content is fully loaded before conversion.

## **Features**

  Extracts fully rendered **HTML & CSS** from ASPX webpages. Supports PDF conversion using PDFKit (via wkhtmltopdf) and WeasyPrint. Automates rendering and extraction with Selenium, ensuring accuracy and document completeness.  

## **Tech Stack**

- Language: Python  
- Libraries: Selenium, PDFKit, WeasyPrint, WebDriver Manager  
- API: N/A  

## **Deployment**

1. Install Python and ensure it is added to your system PATH.
2. Create and activate a virtual environment:
    - python -m venv ASPXScraper
    - Windows: venv\Scripts\activate
    - macOS/Linux: source venv/bin/activate
3. Install dependencies: pip install -r requirements.txt
4. Install wkhtmltopdf:
    - Windows: Download from wkhtmltopdf.org and install it. Ensure the bin folder is added to your system PATH.
    - Linux: sudo apt install wkhtmltopdf
    - macOS: brew install wkhtmltopdf
5. Ensure your desired URL is placed accordingly in line 79. You may also switch between PDFKit and WeasyPrint in line 81.
6. Run the program: python convert_aspx_to_pdf.py
7. The script generates a PDF from an ASPX webpage and saves it as output.pdf in the working directory.
