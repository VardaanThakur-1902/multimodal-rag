class MetadataBuilder:

    @staticmethod
    def build(document):

        return {
            "page_count": len(document.pages),
            "table_count": len(document.tables),
            "image_count": len(document.images),
        }