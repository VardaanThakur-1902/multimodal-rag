import fitz


class PageAnalyzer:

    @staticmethod
    def has_images(page):

        return len(page.get_images()) > 0

    @staticmethod
    def is_scanned(text, page):

        if len(text.strip()) > 30:
            return False

        if len(page.get_images()) > 0:
            return True

        return False

    @staticmethod
    def word_count(text):

        return len(text.split())

    @staticmethod
    def character_count(text):

        return len(text)