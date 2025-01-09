from fpdf import FPDF
import pandas as pd
import os
import sys

sys.path.append(os.path.join(os.getcwd(), "dp100", "src"))

from file_read import FileReader


class PDFGenerator:
    ALIGNMENT = "L"
    SIZE = 8  # 6 works for all; 8 is comfortable
    LINESPACE = 3
    HEIGHT = 74
    WIDTH = 105
    trash_cards = []

    def __init__(self):
        self.pdf = self._get_pdf()

    def _get_pdf(self):
        height, width = self.HEIGHT, self.WIDTH
        pdf = FPDF(orientation="L", unit="mm", format=(height, width))

        # pdf.set_xy(5, 5)

        pdf.set_top_margin(5)
        pdf.set_auto_page_break(auto=False, margin=5)
        pdf.set_left_margin(5)

        return pdf

    def write_flashcards(self, questions_answers):
        pdf = self.pdf
        alignment = self.ALIGNMENT
        size = self.SIZE
        linespace = self.LINESPACE
        page_counter = 0

        for text in questions_answers:
            page_text_size = size
            pdf.set_font("Arial", size=page_text_size)
            while True:
                pdf.add_page()
                pdf.multi_cell(
                    0,
                    linespace,
                    text.encode("utf-8").decode("unicode_escape"),
                    align=alignment,
                )
                if pdf.get_y() < self.HEIGHT:
                    break
                page_text_size -= 1
                self.trash_cards.append(page_counter)
                page_counter += 1
                pdf.set_font("Arial", size=page_text_size)

            page_text_size = self.SIZE
            page_counter += 1

    def save_dummy_pdf(self, filename="dummy_flashcards_a7.pdf"):
        self.pdf.output(filename)
        print(f"Dummy PDF saved as {filename}")

    def save_pdf_file(self, filename="flashcards_a7.pdf"):
        dummy_filename = "dummy_flashcards_a7.pdf"
        self.save_dummy_pdf(dummy_filename)

        from PyPDF2 import PdfWriter, PdfReader

        infile = PdfReader("flashcards_a7.pdf", "rb")
        output = PdfWriter()

        for i in range(len(infile.pages)):
            if i not in self.trash_cards:
                p = infile.pages[i]
                output.add_page(p)

        with open(filename, "wb") as f:
            output.write(f)
        print(f"PDF saved as {filename}")

        os.remove(dummy_filename)
        print(f"Dummy PDF removed")
