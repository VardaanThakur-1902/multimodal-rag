from pathlib import Path

from loaders.pdf_loader import PDFLoader


def main():

    pdf_path = Path("uploads/pdf/sample.pdf")

    if not pdf_path.exists():
        print("PDF not found!")
        return

    loader = PDFLoader()

    document = loader.load(str(pdf_path))

    print("=" * 80)
    print("DOCUMENT METADATA")
    print("=" * 80)

    for key, value in document.metadata.items():
        print(f"{key}: {value}")

    print()

    print("=" * 80)
    print(f"TOTAL PAGES : {len(document.pages)}")
    print(f"TOTAL TABLES: {len(document.tables)}")
    print("=" * 80)

    for page in document.pages:

        print(f"\nPage {page.page_number}")

        print("-" * 40)

        print(f"Has Text       : {page.has_text}")
        print(f"Has Images     : {page.has_images}")
        print(f"Has Tables     : {page.has_tables}")
        print(f"Is Scanned     : {page.is_scanned}")
        print(f"Word Count     : {page.word_count}")
        print(f"Character Count: {page.character_count}")

        print("\nPreview:")

        print(page.text[:200])

        print("\n" + "=" * 80)

    print("\n")

    print("=" * 80)
    print("TABLES")
    print("=" * 80)

    if not document.tables:
        print("No tables found.")

    for table in document.tables:

        print(f"\nPage: {table.page_number}")

        print(f"Table: {table.table_index}")

        print(f"Rows: {table.rows}")

        print(f"Columns: {table.columns}")

        print()

        print(table.markdown)

        print("-" * 80)


if __name__ == "__main__":
    main()