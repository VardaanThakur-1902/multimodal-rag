from pathlib import Path

from loaders.pdf_loader import PDFLoader
from processing.pipeline import (
    ProcessingPipeline,
)

from vectordb.chroma_manager import (
    ChromaManager,
)


def main():

    loader = PDFLoader()

    document = loader.load(
        "uploads/pdf/sample.pdf"
    )

    chunks = ProcessingPipeline.process(
        document
    )

    chroma = ChromaManager()

    chroma.add_chunks(chunks)

    print()

    print("Chunks Added :", len(chunks))

    print(
        "Collection Size :",
        chroma.count(),
    )


if __name__ == "__main__":
    main()