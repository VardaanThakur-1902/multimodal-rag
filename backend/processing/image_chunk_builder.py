from schemas.image_caption import ImageCaption
from schemas.image_chunk import ImageChunk


class ImageChunkBuilder:

    @staticmethod
    def build(
        captions: list[ImageCaption],document_id: str,
    ) -> list[ImageChunk]:

        chunks = []

        for caption in captions:

            chunks.append(

                ImageChunk(

                    document_name=caption.document_name,

                    page_number=caption.page_number,

                    image_path=caption.image_path,

                    caption=caption.caption,

                    metadata={

                        "document_id": document_id,

                        "document_name": caption.document_name,

                        "page": caption.page_number,

                        "chunk_type": "image",

                        "image_path": caption.image_path,


                    },

                )
            )
            print("=" * 50)
            print("IMAGE CHUNK CREATED")
            print("Caption:")
            print(caption.caption)
            print("=" * 50)

        return chunks