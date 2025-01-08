from fpdf import FPDF
import pandas as pd


class FileReader:
    filepath: str = "./dp100/qs_as.xlsx"
    # Qs

    def __init__(self):
        df = pd.read_excel(self.filepath)
        self.Qs = df["questions"].values
        self.As = df["questions"].values

    def __call__(self, *args, **kwds):
        return self.Qs, self.As


class PDFGenerator:

    def __init__(self):
        self.pdf = FPDF(orientation="L", unit="mm", format=(74, 105))

        self.alignment = "L"
        self.size = 8
        self.linespace = 3

    def write_flashcards(self, questions, answers):
        pdf = self.pdf
        alignment = self.alignment
        size = self.size
        linespace = self.linespace

        for question, answer in zip(questions, answers):
            # question side
            pdf.add_page()
            pdf.set_font("Arial", size=size)
            pdf.multi_cell(0, linespace, question, align=alignment)

            # answer side
            pdf.add_page()
            pdf.multi_cell(0, linespace, answer, align=alignment)

    def save_pdf_file(self, filename="flashcards_a7.pdf"):
        self.pdf.output(filename)
        print(f"Flashcards saved to {filename}")


questions, answers = FileReader()()

pdf = PDFGenerator()

pdf.write_flashcards(questions, answers)

pdf.save_pdf_file()
