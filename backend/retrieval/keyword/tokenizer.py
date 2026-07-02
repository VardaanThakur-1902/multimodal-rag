import re


class Tokenizer:

    @staticmethod
    def tokenize(text: str) -> list[str]:

        text = text.lower()

        text = re.sub(r"[^a-z0-9\s]", " ", text)

        return text.split()