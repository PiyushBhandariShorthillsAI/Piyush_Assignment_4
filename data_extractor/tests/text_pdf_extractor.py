import unittest
from unittest.mock import MagicMock
from data_extractor.data_extractor.extractor import Extractor
from data_extractor.data_extractor.pdf_extractor import PDFExtractor

class TestPDFTextExtraction(unittest.TestCase):
    
    def setUp(self):
        # Set up a mock loader to simulate PDF file loading
        self.loader = MagicMock()
        
        # Sample file path
        self.pdf_path = "files/Aman_resume.pdf"
        
        # Create an instance of PDFExtractor with the mock loader
        self.extractor = PDFExtractor(loader=self.loader)
        
        # Sample text that the PDF should return when extracted
        self.expected_text = "This is a sample PDF file containing text on multiple pages."
        
        # Simulate the loader loading a PDF with pages that return the expected text
        mock_pdf = MagicMock()
        mock_pdf.pages = [MagicMock(), MagicMock()]  # Simulate two pages
        
        # Page 1 mock: returning some sample text
        mock_pdf.pages[0].extract_text.return_value = "This is a sample PDF file "
        # Page 2 mock: returning the remaining text
        mock_pdf.pages[1].extract_text.return_value = "containing text on multiple pages."
        
        # Set the loader's load_file method to return this mock PDF
        self.loader.load_file.return_value = mock_pdf
    
    def test_extract_text(self):
        # Load the sample PDF file
        self.extractor.load(self.pdf_path)
        
        # Extract text from the loaded PDF
        extracted_text = self.extractor.extract_text()
        
        # Compare the extracted text with the expected text
        self.assertEqual(extracted_text.strip(), self.expected_text.strip())

if __name__ == '__main__':
    unittest.main()
