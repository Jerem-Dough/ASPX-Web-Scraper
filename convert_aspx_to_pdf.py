import time
import pdfkit
import weasyprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class ASPXToPDFConverter:
    def __init__(self, url, output_pdf="output.pdf"):
        self.url = url
        self.output_pdf = output_pdf
        self.driver = None
        self.config = None

    def setup_driver(self):
        """Set up Selenium WebDriver with headless Chrome."""
        options = Options()
        options.add_argument("--headless")  # Run without opening a window
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def get_page_source(self):
        """Use Selenium to extract the rendered HTML."""
        print("Loading page:", self.url)
        self.driver.get(self.url)
        time.sleep(5)  # Allow time for JavaScript content to load

        html_content = self.driver.page_source  # Extract the rendered page source
        self.driver.quit()
        return html_content

    def save_html_to_file(self, html_content, filename="page.html"):
        """Save the extracted HTML to a source file."""
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_content)
        print("HTML saved to:", filename)
        return filename

    def convert_to_pdf_pdfkit(self, html_filename):
        """Use PDFKit to convert the extracted HTML to PDF."""
        try:
            print("Converting HTML to PDF with PDFKit...")
            self.config = pdfkit.configuration(wkhtmltopdf="wkhtmltopdf")  # Ensure wkhtmltopdf is found
            pdfkit.from_file(html_filename, self.output_pdf, configuration=self.config)
            print(f"PDF saved successfully: {self.output_pdf}")
        except Exception as e:
            print("Error during PDF conversion with PDFKit:", e)

    def convert_to_pdf_weasyprint(self, html_filename):
        """Use WeasyPrint to convert the extracted HTML to PDF (Alternative)."""
        try:
            print("Converting HTML to PDF with WeasyPrint...")
            with open(html_filename, "r", encoding="utf-8") as f:
                html_content = f.read()
            pdf = weasyprint.HTML(string=html_content).write_pdf()
            with open(self.output_pdf, "wb") as f:
                f.write(pdf)
            print(f"PDF saved successfully: {self.output_pdf}")
        except Exception as e:
            print("Error during PDF conversion with WeasyPrint:", e)

    def run(self, use_weasyprint=False):
        """Main function to scrape and convert an ASPX page to PDF."""
        self.setup_driver()
        html_content = self.get_page_source()
        html_filename = self.save_html_to_file(html_content)

        if use_weasyprint:
            self.convert_to_pdf_weasyprint(html_filename)
        else:
            self.convert_to_pdf_pdfkit(html_filename)

if __name__ == "__main__":
    url = "Enter your URL here!" # Enter your URL here, ensure site does not require login credentials!
    converter = ASPXToPDFConverter(url, "output.pdf")
    converter.run(use_weasyprint=True) # When false, PDFKit will be used to convert HTML to PDF. 
                                       # When true, WeasyPrint will be used to convert HTML to PDF. 
