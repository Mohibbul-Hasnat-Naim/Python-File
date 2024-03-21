# # Example usage
# input_folder = 'H:/DIU/9th Semester/RE Lab'  # Path to folder containing PDF files
# cover_page_path = 'H:/DIU/9th Semester/RE Lab/RE Covr Page Lab.pdf'  # Path to cover page PDF file
# output_folder = 'H:/DIU/9th Semester/RE Lab/RE Lab'  # Path for the output folder

import os
import fitz  # PyMuPDF

def add_cover_page_to_folder(input_folder, cover_page_path, output_folder):
    # Open the cover page
    cover_document = fitz.open(cover_page_path)
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over each PDF file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_pdf_path = os.path.join(input_folder, filename)
            output_pdf_path = os.path.join(output_folder, filename)
            
            # Open the existing PDF
            pdf_document = fitz.open(input_pdf_path)
            
            # Create a new PDF document with the cover page
            output_document = fitz.open()
            output_document.insert_pdf(cover_document)
            
            # Add the pages from the existing PDF to the new document
            output_document.insert_pdf(pdf_document)
            
            # Save the new document with the cover page
            output_document.save(output_pdf_path)
            
            # Close the documents
            pdf_document.close()
            output_document.close()
    
    # Close the cover page document
    cover_document.close()

# Example usage
input_folder = 'H:/DIU/9th Semester/RE Lab'  # Path to folder containing PDF files
cover_page_path = 'H:/DIU/9th Semester/RE Lab/RE Covr Page Lab.pdf'  # Path to cover page PDF file
output_folder = 'H:/DIU/9th Semester/RE Lab/RE Lab'  # Path for the output folder

add_cover_page_to_folder(input_folder, cover_page_path, output_folder)
print("Add cover page successfully!")