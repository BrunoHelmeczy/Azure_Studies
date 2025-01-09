import pandas as pd


class FileReader:
    filepath: str = "./dp100/data/flashcards/raw.txt"

    def __init__(self):
        self.df = self.get_data()

    def __call__(self):
        return self.df

    def _read_raw_file(self, filepath: str) -> pd.DataFrame:

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().replace("\n", " ")

        return content

    def _split_sections(self, content: str) -> pd.DataFrame:
        import re

        regex = re.compile(r"(?:PRACTICE TEST \d+ . (?:QUESTIONS|ANSWERS) ONLY)")
        sections = regex.findall(content)
        pts = regex.split(content)

        split_text = [segment for segment in pts if segment.strip()]

        df = pd.DataFrame({"section": sections, "content": split_text})

        return df

    def _clean_metadata(self, df: pd.DataFrame) -> pd.DataFrame:
        df["practice_test_id"] = (
            df["section"].str.extract(r"PRACTICE TEST (\d+)").astype(int)
        )

        df["section"] = df["section"].str.extract(r"(QUESTIONS|ANSWERS) ONLY")
        df["section"] = df["section"].str.lower()

        return df.reindex(columns=["practice_test_id", "section", "content"])

    def _split_questions_answers(self, df: pd.DataFrame) -> pd.DataFrame:
        df["question_nrs"] = df["content"].str.findall("QUESTION (\d+)")
        df["q_contents"] = (
            df["content"].str.strip().str.split("QUESTION \d+").apply(lambda x: x[1:])
        )

        df.drop(columns="content", inplace=True)

        df = df.explode(["question_nrs", "q_contents"])
        df["question_nrs"] = df["question_nrs"].astype(int)
        # add new line character before answer choices
        df["q_contents"] = (
            df["q_contents"].str.strip().str.replace(r"(?=[A-F]\))", "\n", regex=True)
        )

        df.sort_values(
            ["practice_test_id", "question_nrs", "section"],
            ascending=[True, True, False],
            inplace=True,
        )

        return df

    def get_data(self) -> pd.DataFrame:

        df = (
            self._split_sections(self._read_raw_file(self.filepath))
            .pipe(self._clean_metadata)
            .pipe(self._split_questions_answers)
            .reset_index(drop=True)
        )

        return df
