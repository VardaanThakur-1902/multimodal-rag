from abc import ABC
from abc import abstractmethod

from schemas.extracted_document import (
    ExtractedDocument,
)


class BaseLoader(ABC):

    @abstractmethod
    def load(
        self,
        file_path: str,
    ) -> ExtractedDocument:
        pass