When copying text into files, especially markdown (`README.md`), the structure can sometimes get distorted due to formatting issues. Here's a way to ensure the structure remains intact:

### Steps to Properly Copy and Paste the README:

1. **Use a Plain Text Editor**:
   Make sure you are pasting the content into a **plain text editor** or directly into your code editor (like VSCode, Sublime Text, or any other editor you're using for the project).

2. **Paste Markdown as Plain Text**:
   When pasting content, sometimes rich text editors (like Word, Google Docs, etc.) can change the formatting. Always paste in a code editor or use the "Paste as Plain Text" option if you're copying from a web interface.

3. **Markdown Preview**:
   If you're using VSCode, you can enable the markdown preview to verify the formatting:
   - Right-click in the `.md` file and choose "Open Preview" or press `Ctrl+Shift+V` (on Windows/Linux) or `Cmd+Shift+V` (on macOS).

4. **Check for Indentation**:
   In markdown, indentation is important for lists, code blocks, and nested items. Ensure that:
   - Lists have the correct number of spaces or tabs (usually 2 or 4 spaces).
   - Code blocks are wrapped with triple backticks (```) for Python or terminal commands.
   - Nested lists/items are properly indented under their parent items.

Here’s the README content again formatted so that you can directly copy it into your file:

---

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
