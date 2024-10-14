import unittest
import os
from data_extractor.data_extractor.docx_extractor import DOCXExtractor
from data_extractor.data_extractor.pdf_extractor import PDFExtractor
from data_extractor.data_extractor.pptx_extractor import PPTXExtractor
from data_extractor.file_loaders.pdf_loader import PDFLoader
from data_extractor.file_loaders.docx_loader import DOCXLoader
from data_extractor.file_loaders.ppt_loader import PPTLoader
from data_extractor.storage.file_storage import FileStorage
from data_extractor.storage.sql_storage import SQLStorage
 
 
class FileExtractionTestBase(unittest.TestCase):
    """Base class for setting up extractors and storage."""
    def setUp(self):
        # Base setup for file extractors
        self.file_storage = FileStorage("test_output")
        self.sql_storage = SQLStorage()
 
    def tearDown(self):
        # Close storages after tests
        self.file_storage.close()
        self.sql_storage.close()
 
    def extract_and_store(self, extractor, file_path):
        extractor.load(file_path)
        extracted_text = extractor.extract_text()
        images = extractor.extract_images()
        urls = extractor.extract_urls()
        tables = extractor.extract_tables()
        # Storing extracted data
        self.file_storage.store(extracted_text, os.path.basename(file_path), 'text')
        if images:
            self.file_storage.store(images, os.path.basename(file_path), 'image')
        if urls:
            self.file_storage.store(urls, os.path.basename(file_path), 'url')
        if tables:
            self.file_storage.store(tables, os.path.basename(file_path), 'table')
        # Return extracted data for assertions
        return {
            'text': extracted_text,
            'images': images,
            'urls': urls,
            'tables': tables
        }

class TestPDFExtraction(FileExtractionTestBase):
    """Test class for PDF extraction."""
 
    def test_pdf_with_text_only(self):
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_text_only.pdf')
 
        self.assertTrue(data['text'])
        self.assertFalse(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_pdf_with_images_only(self):
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_images_only.pdf')
 
        self.assertFalse(data['text'])
        self.assertTrue(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_pdf_with_tables_only(self):
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_tables_only.pdf')
 
        self.assertFalse(data['text'])
        self.assertFalse(data['images'])
        self.assertFalse(data['urls'])
        self.assertTrue(data['tables'])
 
    def test_pdf_with_text_and_images(self):
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_text_images.pdf')
 
        self.assertTrue(data['text'])
        self.assertTrue(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_pdf_with_text_images_tables_urls(self):
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_text_images_tables_urls.pdf')
 
        self.assertTrue(data['text'])
        self.assertTrue(data['images'])
        self.assertTrue(data['urls'])
        self.assertTrue(data['tables'])
 
    def test_pdf_with_empty_file(self):
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_empty.pdf')
 
        self.assertFalse(data['text'])
        self.assertFalse(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_pdf_with_large_file(self):
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_large.pdf')
 
        self.assertTrue(data['text'])
        self.assertTrue(data['images'])
        self.assertTrue(data['urls'])
        self.assertTrue(data['tables'])
 
    def test_pdf_with_corrupted_file(self):
        loader = PDFLoader()
        extractor = PDFExtractor(loader)
        with self.assertRaises(ValueError):
            self.extract_and_store(extractor, 'test_files/test_corrupted.pdf')
 
 
class TestDOCXExtraction(FileExtractionTestBase):
    """Test class for DOCX extraction."""
 
    def test_docx_with_text_only(self):
        loader = DOCXLoader()
        extractor = DOCXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_text_only.docx')
 
        self.assertTrue(data['text'])
        self.assertFalse(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_docx_with_images_only(self):
        loader = DOCXLoader()
        extractor = DOCXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_images_only.docx')
 
        self.assertFalse(data['text'])
        self.assertTrue(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_docx_with_tables_only(self):
        loader = DOCXLoader()
        extractor = DOCXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_tables_only.docx')
 
        self.assertFalse(data['text'])
        self.assertFalse(data['images'])
        self.assertFalse(data['urls'])
        self.assertTrue(data['tables'])
 
    def test_docx_with_text_and_images(self):
        loader = DOCXLoader()
        extractor = DOCXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_text_images.docx')
 
        self.assertTrue(data['text'])
        self.assertTrue(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_docx_with_text_images_tables_urls(self):
        loader = DOCXLoader()
        extractor = DOCXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_text_images_tables_urls.docx')
 
        self.assertTrue(data['text'])
        self.assertTrue(data['images'])
        self.assertTrue(data['urls'])
        self.assertTrue(data['tables'])
 
    def test_docx_with_empty_file(self):
        loader = DOCXLoader()
        extractor = DOCXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_empty.docx')
 
        self.assertFalse(data['text'])
        self.assertFalse(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_docx_with_large_file(self):
        loader = DOCXLoader()
        extractor = DOCXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_large.docx')
 
        self.assertTrue(data['text'])
        self.assertTrue(data['images'])
        self.assertTrue(data['urls'])
        self.assertTrue(data['tables'])
 
    def test_docx_with_corrupted_file(self):
        loader = DOCXLoader()
        extractor = DOCXExtractor(loader)
        with self.assertRaises(ValueError):
            self.extract_and_store(extractor, 'test_files/test_corrupted.docx')
 
 
class TestPPTXExtraction(FileExtractionTestBase):
    """Test class for PPTX extraction."""
 
    def test_pptx_with_text_only(self):
        loader = PPTLoader()
        extractor = PPTXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_text_only.pptx')
 
        self.assertTrue(data['text'])
        self.assertFalse(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_pptx_with_images_only(self):
        loader = PPTLoader()
        extractor = PPTXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_images_only.pptx')
 
        self.assertFalse(data['text'])
        self.assertTrue(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_pptx_with_text_and_images(self):
        loader = PPTLoader()
        extractor = PPTXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_text_images.pptx')
 
        self.assertTrue(data['text'])
        self.assertTrue(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_pptx_with_empty_file(self):
        loader = PPTLoader()
        extractor = PPTXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_empty.pptx')
 
        self.assertFalse(data['text'])
        self.assertFalse(data['images'])
        self.assertFalse(data['urls'])
        self.assertFalse(data['tables'])
 
    def test_pptx_with_large_file(self):
        loader = PPTLoader()
        extractor = PPTXExtractor(loader)
        data = self.extract_and_store(extractor, 'test_files/test_large.pptx')
 
        self.assertTrue(data['text'])
        self.assertTrue(data['images'])
        self.assertTrue(data['urls'])
        self.assertTrue(data['tables'])
 
    def test_pptx_with_corrupted_file(self):
        loader = PPTLoader()
        extractor = PPTXExtractor(loader)
        with self.assertRaises(ValueError):
            self.extract_and_store(extractor, 'test_files/test_corrupted.pptx')