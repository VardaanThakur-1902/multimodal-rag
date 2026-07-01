from schemas.chunk import Chunk


class Chunker:

    @staticmethod
    def chunk(document):

        chunks = []

        # ---------- Text ----------

        for page in document.pages:

            if page.text.strip():

                chunks.append(

                    Chunk(
                        document_name=document.metadata.get(
                            "source_file",
                            "Unknown"
                        ),

                        page_number=page.page_number,

                        chunk_type="text",

                        content=page.text,

                        metadata={
                            "page": page.page_number,
                            "type": "text",
                        }
                    )

                )


        # ---------- Tables ----------

        for table in document.tables:

            chunks.append(

                Chunk(
                    document_name=document.metadata.get(
                        "source_file",
                        "Unknown"
                    ),

                    page_number=table.page_number,

                    chunk_type="table",

                    content=table.markdown,

                    metadata={
                        "page": table.page_number,
                        "type": "table",
                        "rows": table.rows,
                        "columns": table.columns,
                    }
                )

            )

        return chunks