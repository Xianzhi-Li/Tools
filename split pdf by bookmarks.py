import PyPDF2
import os
import time
import shutil
import argparse

# Helper class used to map pages numbers to bookmarks
class BookmarkToPageMap:
    def __init__(self, pdf_reader):
        self.reader = pdf_reader

    def get_destination_page_numbers(self):
        """
        Extract the page numbers associated with each bookmark in the PDF.
        Returns a dictionary with the bookmark title as key and page number as value.
        """
        def _get_bookmark_page_numbers(bookmark_list, reader):
            result = []
            for item in bookmark_list:
                if isinstance(item, list):
                    result.extend(_get_bookmark_page_numbers(item, reader))
                else:
                    result.append({'PageNumber': reader.get_destination_page_number(item),
                                   'Title': item.title})
            return result

        bookmarks = _get_bookmark_page_numbers(self.reader.outline, self.reader)
        return {bookmark['Title']: bookmark['PageNumber'] for bookmark in bookmarks}

def split_pdf_by_bookmarks(sourcePDFFile, outputPDFDir, outputNamePrefix, deleteSourcePDF):
    targetPDFFile = 'temppdfsplitfile.pdf'

    # Ensure output directory exists
    if not os.path.exists(outputPDFDir):
        os.makedirs(outputPDFDir)

    print('Parameters:')
    print(f"Source PDF: {sourcePDFFile}")
    print(f"Source PDF file name: {base_name}")
    print(f"Output Directory: {outputPDFDir}")
    print(f"Output Name Prefix: {outputNamePrefix}")
    print(f"Temporary PDF File: {targetPDFFile}")

    # Verify that the source PDF exists
    while not os.path.exists(sourcePDFFile):
        print('Source PDF not found, sleeping...')
        time.sleep(10)

    if os.path.exists(sourcePDFFile):
        print('Found source PDF file')
        shutil.copy(sourcePDFFile, targetPDFFile)

        with open(targetPDFFile, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            bookmark_map = BookmarkToPageMap(pdf_reader)

            # Get total pages
            number_of_pages = len(pdf_reader.pages)
            print(f'PDF # Pages: {number_of_pages}')

            # Get the bookmark to page number mapping
            bookmarks = bookmark_map.get_destination_page_numbers()

            prev_page_num = 0
            prev_page_name = None

            for bookmark_title, page_num in sorted(bookmarks.items(), key=lambda x: x[1]):
                print(f'Processing: {bookmark_title} at page {page_num}')

                # Save the section between the previous bookmark and the current one
                if prev_page_name is not None:
                    write_pdf(pdf_reader, prev_page_num, page_num, outputPDFDir, outputNamePrefix, prev_page_name)

                prev_page_num = page_num
                prev_page_name = bookmark_title

            # Handle the final section from the last bookmark to the end of the PDF
            if prev_page_name is not None:
                write_pdf(pdf_reader, prev_page_num, number_of_pages, outputPDFDir, outputNamePrefix, prev_page_name)

        # Delete temporary file
        os.remove(targetPDFFile)

        if deleteSourcePDF.lower() == "true":
            os.remove(sourcePDFFile)
            print(f"Source PDF file '{sourcePDFFile}' deleted.")

def write_pdf(pdf_reader, start_page, end_page, output_dir, prefix, title):
    """
    Writes a portion of the PDF to a new file.
    :param pdf_reader: PdfReader object
    :param start_page: Start page number (1-indexed)
    :param end_page: End page number (1-indexed)
    :param output_dir: Output directory for the new PDF file
    :param prefix: Prefix for the new PDF filename
    :param title: Title of the section to be used in the filename
    """
    pdf_writer = PyPDF2.PdfWriter()
    title_sanitized = title.replace(':', '_').replace('*', '_').replace('/', ' ')

    # Adjust start_page and end_page to ensure the correct pages are included.
    for i in range(start_page, end_page):
        pdf_writer.add_page(pdf_reader.pages[i])

    output_filename = os.path.join(output_dir, f"{prefix}_{title_sanitized}.pdf")
    with open(output_filename, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"Created PDF file: {output_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input PDF file")
    parser.add_argument("output", nargs="?", help="output directory for the split files", default="./output/")
    parser.add_argument("delete", nargs="?", help="delete the original file? (True/False)", default="False")
    args = parser.parse_args()

    # Extract the base name of the input PDF for output prefix and directory
    base_name = os.path.splitext(os.path.basename(args.input))[0]
    output_directory = os.path.join(args.output, base_name)

    # Call the split function with derived prefix and directory
    split_pdf_by_bookmarks(args.input, output_directory, base_name, args.delete)
