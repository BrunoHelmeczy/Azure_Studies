import os
import sys

sys.path.append(os.path.join(os.getcwd(), "dp100", "src"))

from file_read import FileReader
from pdf_generator import PDFGenerator

data = FileReader()()["q_contents"]

pdf = PDFGenerator()

pdf.write_flashcards(data)

pdf.save_pdf_file()
