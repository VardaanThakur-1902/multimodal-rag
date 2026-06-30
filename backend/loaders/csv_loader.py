from loaders.base_loader import BaseLoader
from schemas.extracted_document import (
    ExtractedDocument,
)


class CSVLoader(BaseLoader):

    def load(
        self,
        file_path: str,
    ) -> ExtractedDocument:

        return ExtractedDocument()