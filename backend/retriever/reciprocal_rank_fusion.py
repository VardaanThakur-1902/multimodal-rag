from collections import defaultdict


class ReciprocalRankFusion:

    @staticmethod
    def fuse(
        vector_results: list[dict],
        bm25_results: list[dict],
        k: int = 60,
    ) -> list[dict]:

        scores = defaultdict(float)
        documents = {}

        # Vector ranking
        for rank, result in enumerate(vector_results):

            chunk_id = (
                result["metadata"]["chunk_id"]
            )

            scores[chunk_id] += 1 / (
                k + rank + 1
            )

            documents[chunk_id] = result

        # BM25 ranking
        for rank, result in enumerate(bm25_results):

            chunk_id = (
                result["metadata"]["chunk_id"]
            )

            scores[chunk_id] += 1 / (
                k + rank + 1
            )

            documents[chunk_id] = result

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True,
        )

        output = []

        for chunk_id, score in ranked:

            result = documents[chunk_id]

            result["rrf_score"] = score

            output.append(result)

        return output