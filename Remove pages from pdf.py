import os
import fitz  # PyMuPDF

def remove_first_pages(input_pdf_path, output_pdf_path):
    pdf_document = fitz.open(input_pdf_path)
    
    if len(pdf_document) < 4:
        print(f"Skipping '{input_pdf_path}' because it has less than 4 pages.")
        return
    
    pdf_document.delete_pages(range(3))  # Remove first three pages
    pdf_document.delete_page(-1)  # Remove last page
    
    pdf_document.save(output_pdf_path)
    pdf_document.close()

# input_folder = "D:/Math Master"
# output_folder = "D:/Math Master/Math Masterv2"


continue_processing = True
while continue_processing:

    input_folder = input("Current file directory: ")
    output_folder = input("Saved file directory: ")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_pdf_path = os.path.join(input_folder, filename)
            output_pdf_path = os.path.join(output_folder, filename)
            remove_first_pages(input_pdf_path, output_pdf_path)
            print(f"Processed '{input_pdf_path}'")
    user_input = input("Page removed Successfully!! \n'ok' to continue or Press Enter to exit...   ")
    if user_input.lower() == "ok":
        continue_processing == True
    else:
        continue_processing = False