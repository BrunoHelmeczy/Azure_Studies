from fpdf import FPDF
import pandas as pd


class PDFGenerator:
    ALIGNMENT = "L"
    SIZE = 8  # 6 works for all; 8 is comfortable
    LINESPACE = 3
    HEIGHT = 74
    WIDTH = 105

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

    def write_flashcards(self, questions, answers):
        pdf = self.pdf
        alignment = self.ALIGNMENT
        size = self.SIZE
        linespace = self.LINESPACE

        for question, answer in zip(questions, answers):
            page_text_size = size
            # question side
            # question = questions[-1]
            pdf.set_font("Arial", size=page_text_size)
            while True:
                pdf.add_page()
                pdf.multi_cell(0, linespace, question, align=alignment)
                if pdf.get_y() < self.HEIGHT:
                    break
                page_text_size -= 1
                pdf.set_font("Arial", size=page_text_size)
                print(page_text_size)
            # pdf.get_x()
            page_text_size = self.SIZE
            print(page_text_size)

            # answer side
            pdf.add_page()
            # page_text_size = 8
            page_text_size = self.SIZE
            pdf.set_font("Arial", size=page_text_size)
            # while pdf.get_string_width(answer) > (pdf.w - 5) or page_text_size >= 6:
            #     page_text_size -= 1
            #     pdf.set_font("Arial", size=page_text_size)
            pdf.multi_cell(0, linespace, answer, align=alignment)

    def save_pdf_file(self, filename="flashcards_a7.pdf"):
        self.pdf.output(filename)
        print(f"Flashcards saved to {filename}")
