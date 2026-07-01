from pathlib import Path

from embeddings.embedding_service import (
    EmbeddingService,
)
from loaders.pdf_loader import PDFLoader
from processing.pipeline import (
    ProcessingPipeline,
)


def main():

    pdf_path = Path(
        "uploads/pdf/sample.pdf"
    )

    loader = PDFLoader()

    document = loader.load(
        str(pdf_path)
    )

    chunks = ProcessingPipeline.process(
        document
    )

    print(f"Chunks: {len(chunks)}")

    embedding = EmbeddingService.generate(
        chunks[0]
    )

    print()

    print(
        "Embedding dimension:",
        len(embedding)
    )

    print()

    print(
        embedding[:10]
    )
    


if __name__ == "__main__":
    main()