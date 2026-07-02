from indexing.indexing_service import IndexingService


def main():

    service = IndexingService()

    result = service.index_document(
        "uploads/pdf/sample.pdf"
    )

    print(result)


if __name__ == "__main__":
    main()