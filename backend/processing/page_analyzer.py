import fitz


class PageAnalyzer:

    @staticmethod
    def has_images(page):
        return len(page.get_images(full=True)) > 0

    @staticmethod
    def is_scanned(text, page):

        text = text.strip()

        # Digital PDF
        if len(text) > 50:
            return False

        # Embedded images
        if len(page.get_images(full=True)) > 0:
            return True

        # Full-page drawing (common in scanned PDFs)
        drawings = page.get_drawings()

        if len(drawings) > 100:
            return True

        return len(text) < 20

    @staticmethod
    def word_count(text):
        return len(text.split())

    @staticmethod
    def character_count(text):
        return len(text)