# PDF Renaming Script (Based on Content)

This script automatically renames PDF files in a given folder by extracting key fields (such as Invoice Number, Name, and Date) from the text content of each PDF.

---

## 🧠 Features

- Extracts content from each PDF using OCR-free parsing (`PyMuPDF`)
- Renames files in the format: `InvoiceNumber_Name_Date.pdf`
- Works with multiple PDF files in a folder
- Cross-platform: Windows, macOS, Linux
- Lightweight, fast, and dependency-free (besides one Python library)

---

## ⚙️ Requirements

- Python 3.6+
- [`PyMuPDF`](https://pymupdf.readthedocs.io/en/latest/) (also known as `fitz`)

Install the library using pip:

```bash
pip install pymupdf
