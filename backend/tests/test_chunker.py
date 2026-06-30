from pathlib import Path

from loaders.pdf_loader import PDFLoader
from processing.pipeline import ProcessingPipeline


def print_document_info(document):

    print("=" * 80)
    print("DOCUMENT")
    print("=" * 80)

    print(f"Pages  : {len(document.pages)}")
    print(f"Tables : {len(document.tables)}")
    print()

    print("Metadata")

    for key, value in document.metadata.items():
        print(f"{key}: {value}")

    print()


def print_chunks(chunks):

    print("=" * 80)
    print("CHUNKS")
    print("=" * 80)

    print(f"Total Chunks: {len(chunks)}")

    for chunk in chunks:

        print("\n")

        print("-" * 80)

        print(f"Chunk ID    : {chunk.chunk_id}")
        print(f"Type        : {chunk.chunk_type}")
        print(f"Page        : {chunk.page_number}")

        print("\nContent Preview\n")

        preview = chunk.content[:400]

        print(preview)

        print("-" * 80)


def main():

    pdf_path = Path("uploads/pdf/sample.pdf")

    if not pdf_path.exists():

        print("Sample PDF not found!")

        return

    loader = PDFLoader()

    document = loader.load(str(pdf_path))

    print_document_info(document)

    chunks = ProcessingPipeline.process(document)

    print_chunks(chunks)


if __name__ == "__main__":
    main()