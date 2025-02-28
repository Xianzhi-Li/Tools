import fitz  # PyMuPDF
import re

def add_bookmarks():
    # Ask for the PDF file name
    pdf_path = input("Enter the PDF file name (including .pdf): ").strip()

    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening file: {e}")
        return

    output_pdf = "output_with_bookmarks.pdf" #name of output file
    chapter_pattern = re.compile(r"CHAPTER OVERVIEW\s*\n(\d+):\s*(.+)", re.IGNORECASE) #should be changed based on specific book
    bookmarks = []
    page_count = len(doc)  # Get total number of pages

    # Scan pages for chapter titles
    for page_num in range(page_count):
        text = doc[page_num].get_text("text")
        match = chapter_pattern.search(text)
        
        if match:
            chapter_num = match.group(1)  # Extracts chapter number
            chapter_title = match.group(2).strip()  # Extracts chapter title
            bookmark_name = f"ch {chapter_num} {chapter_title}"
            print(f"Detected: {bookmark_name} on page {page_num + 1}")

            # Ensure page number is an integer (1-based index for PDF bookmarks)
            bookmarks.append([1, bookmark_name, page_num + 1])

    # Apply bookmarks using set_toc()
    if bookmarks:
        try:
            doc.set_toc(bookmarks)
            doc.save(output_pdf)
            print(f"Bookmarks added and saved as {output_pdf}")
        except Exception as e:
            print(f"Error applying TOC: {e}")
    else:
        print("No chapters detected.")

# Run the function
add_bookmarks()
