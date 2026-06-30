from schemas.chunk import Chunk


class Chunker:

    @staticmethod
    def chunk(document):

        chunks = []

        chunk_id = 1

        # ---------- Text ----------

        for page in document.pages:

            if page.text.strip():

                chunks.append(

                    Chunk(
                        chunk_id=chunk_id,
                        page_number=page.page_number,
                        content=page.text,
                        chunk_type="text",
                    )

                )

                chunk_id += 1

        # ---------- Tables ----------

        for table in document.tables:

            chunks.append(

                Chunk(
                    chunk_id=chunk_id,
                    page_number=table.page_number,
                    content=table.markdown,
                    chunk_type="table",
                )

            )

            chunk_id += 1

        return chunks