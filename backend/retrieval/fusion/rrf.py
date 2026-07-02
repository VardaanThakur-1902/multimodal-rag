from schemas.retrieval_result import RetrievalResult


class ReciprocalRankFusion:

    @staticmethod
    def fuse(
        vector_results: list[RetrievalResult],
        keyword_results: list[RetrievalResult],
        k: int = 60,
    ) -> list[RetrievalResult]:

        scores = {}
        objects = {}

        for rank, result in enumerate(vector_results):

            chunk_id = result.chunk_id

            scores[chunk_id] = (
                scores.get(chunk_id, 0)
                + 1 / (k + rank + 1)
            )

            objects[chunk_id] = result

        for rank, result in enumerate(keyword_results):

            chunk_id = result.chunk_id

            scores[chunk_id] = (
                scores.get(chunk_id, 0)
                + 1 / (k + rank + 1)
            )

            objects[chunk_id] = result

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        final_results = []

        for chunk_id, score in ranked:

            result = objects[chunk_id]

            result.score = score

            final_results.append(result)

        return final_results