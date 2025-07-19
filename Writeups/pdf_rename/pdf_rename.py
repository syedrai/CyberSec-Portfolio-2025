import os
import fitz  # PyMuPDF
import re

def extract_fields_from_text(text):
    # Adjust these regex patterns based on actual PDF content
    invoice_match = re.search(r"Invoice[:\s]*([A-Za-z0-9-]+)", text)
    name_match = re.search(r"Name[:\s]*([A-Za-z ]+)", text)
    date_match = re.search(r"Date[:\s]*([\d/-]+)", text)

    invoice = invoice_match.group(1).strip() if invoice_match else "UnknownInvoice"
    name = name_match.group(1).strip().replace(" ", "_") if name_match else "UnknownName"
    date = date_match.group(1).strip().replace("/", "-") if date_match else "UnknownDate"

    return invoice, name, date

def rename_pdfs_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            old_path = os.path.join(folder_path, filename)
            try:
                doc = fitz.open(old_path)
                text = ""
                for page in doc:
                    text += page.get_text()
                doc.close()

                invoice, name, date = extract_fields_from_text(text)
                new_filename = f"{invoice}_{name}_{date}.pdf"
                new_path = os.path.join(folder_path, new_filename)

                os.rename(old_path, new_path)
                print(f"Renamed: {filename} → {new_filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

# === USAGE ===
# Replace below path with your PDF folder path
rename_pdfs_in_folder("/path/to/your/pdf/folder")
