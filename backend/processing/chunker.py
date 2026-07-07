from schemas.chunk import Chunk
from processing.text_splitter import TextSplitter


class Chunker:

    @staticmethod
    def chunk(
        document,
        
    ):

        chunks = []

        # ---------- Text ----------

        for page in document.pages:

            if not page.text.strip():
                continue

            text_chunks = TextSplitter.split(
                page.text
            )

            for chunk_text in text_chunks:

                chunks.append(

                    Chunk(
                        document_name=document.metadata.get(
                            "source_file",
                            "Unknown"
                        ),
                        page_number=page.page_number,
                        chunk_type="text",
                        content=chunk_text,
                        metadata={
                            "page": page.page_number,
                            "chunk_type": "text",
                            "document_name": document.metadata.get(
                                "source_file",
                                "Unknown"
                            ),
                        },
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
                        "document_name": document.metadata.get(
                            "source_file",
                            "Unknown",
                        ),
                        "page": table.page_number,
                        "chunk_type": "table",
                        "rows": table.rows,
                        "columns": table.columns,
                    }
                )

            )

        return chunks