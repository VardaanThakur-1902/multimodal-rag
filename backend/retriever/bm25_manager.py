from rank_bm25 import BM25Okapi

from schemas.chunk import Chunk


class BM25Manager:

    _bm25 = None

    _chunks = []

    @classmethod
    def build(
        cls,
        chunks: list[Chunk],
    ):

        cls._chunks = chunks

        corpus = [
            chunk.content.lower().split()
            for chunk in chunks
        ]

        cls._bm25 = BM25Okapi(corpus)

    @classmethod
    def is_ready(cls):

        return cls._bm25 is not None

    @classmethod
    def get_bm25(cls):

        return cls._bm25

    @classmethod
    def get_chunks(cls):

        return cls._chunks