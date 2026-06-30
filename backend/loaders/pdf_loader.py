import fitz

from loaders.base_loader import BaseLoader
from processing.page_analyzer import PageAnalyzer
from schemas.extracted_document import ExtractedDocument
from schemas.page import PageData
from tables.pdf_tables import PDFTableExtractor


class PDFLoader(BaseLoader):

    def load(
        self,
        file_path: str,
    ) -> ExtractedDocument:

        pdf = fitz.open(file_path)

        pages = []

        full_text = []

        # -----------------------------
        # Extract Tables
        # -----------------------------

        tables = PDFTableExtractor.extract(file_path)

        table_pages = {
            table.page_number
            for table in tables
        }

        # -----------------------------
        # Process Each Page
        # -----------------------------

        for index, page in enumerate(pdf):

            text = page.get_text("text")

            page_data = PageData(
                page_number=index + 1,

                text=text,

                has_text=len(text.strip()) > 0,

                has_images=PageAnalyzer.has_images(
                    page
                ),

                has_tables=(index + 1)
                in table_pages,

                is_scanned=PageAnalyzer.is_scanned(
                    text,
                    page,
                ),

                word_count=PageAnalyzer.word_count(
                    text
                ),

                character_count=PageAnalyzer.character_count(
                    text
                ),
            )

            pages.append(page_data)

            full_text.append(text)

        # -----------------------------
        # Metadata
        # -----------------------------

        metadata = pdf.metadata or {}

        metadata["page_count"] = len(pdf)

        metadata["table_count"] = len(tables)

        metadata["image_pages"] = sum(
            page.has_images
            for page in pages
        )

        metadata["scanned_pages"] = sum(
            page.is_scanned
            for page in pages
        )

        metadata["has_tables"] = (
            len(tables) > 0
        )

        pdf.close()

        # -----------------------------
        # Return Extracted Document
        # -----------------------------

        return ExtractedDocument(

            text="\n".join(full_text),

            pages=pages,

            tables=tables,

            metadata=metadata,

        )