from loaders.pdf_loader import PDFLoader
from processing.pipeline import ProcessingPipeline
from vectordb.chroma_manager import ChromaManager
from retrieval.retrieval_service import RetrievalService

class IndexingService:

    def __init__(self):

        self.loader = PDFLoader()

        self.vector_db = ChromaManager()

        self.retrieval = RetrievalService()

    def index_document(
        self,
        file_path: str,
    ) -> dict:

        # Load document
        document = self.loader.load(file_path)

        # Process into chunks
        chunks = ProcessingPipeline.process(document)

        # Store in ChromaDB
        self.vector_db.add_chunks(chunks)

        self.retrieval.build_index(chunks)

        return {
            "document_name": document.document_name,
            "pages": len(document.pages),
            "tables": len(document.tables),
            "chunks": len(chunks),
        }

    def load_document(
        self,
        file_path: str,
    ):
        """
        Load a document without indexing.
        Useful for testing.
        """

        return self.loader.load(file_path)

    def process_document(
        self,
        file_path: str,
    ):
        """
        Load + process a document into chunks
        without storing them.
        Useful for BM25 tests.
        """

        document = self.loader.load(file_path)

        chunks = ProcessingPipeline.process(document)

        return chunks

    def index_chunks(
        self,
        chunks,
    ):
        """
        Store already-created chunks in ChromaDB.
        """

        self.vector_db.add_chunks(chunks)

    def collection_size(
        self,
    ) -> int:

        return self.vector_db.count()