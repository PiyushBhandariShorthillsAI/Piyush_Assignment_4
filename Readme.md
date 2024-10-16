
# Python Data Extractor for PDF, PPT, and DOCX

## Project Overview
This project is a Python-based data extraction application that extracts content such as text, images, hyperlinks, and tables from files in **PDF**, **PPT**, and **DOCX** formats.

The project structure is organized as follows:
```
data_extractor/
    ├── data_extractor/
    │   ├── docx_extractor.py
    │   ├── extractor.py
    │   ├── pdf_extractor.py
    │   ├── pptx_extractor.py
    ├── file_loaders/
    │   ├── docx_loader.py
    │   ├── file_loader.py
    │   ├── pdf_loader.py
    │   ├── ppt_loader.py
    ├── storage/
    │   ├── file_storage.py
    │   ├── sql_storage.py
    ├── tests/
    │   ├── test_pdf_extractor.py
    │   ├── test_pdf_loader.py
```

## Features
The **data extraction** module contains methods for:
- Extracting **text** from PDF, PPT, DOCX files.
- Extracting **images** from files.
- Extracting **links** or hyperlinks embedded in files.
- Extracting **tables** from documents.

The project also supports storing extracted data in:
- **File-based storage** (via `file_storage.py`).
- **SQL database storage** (via `sql_storage.py`).

## Running the Project
To run the project, you need to execute the `main.py` file. This will initialize the extraction and storage processes.

Use the following command to run the project:
```bash
python3 main.py
```

## Project Dependencies
The following dependencies are required to run the project:
- `python-docx`
- `PyPDF2`
- `python-pptx`
- `pdfplumber`
- `fitz`

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

## Testing
The `tests/` folder contains unit test cases for the different functionalities of the data extractor. To run the tests, use:
```bash
python3 -m unittest discover -s tests
```

---
