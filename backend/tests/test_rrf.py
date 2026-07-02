from retriever.reciprocal_rank_fusion import (
    ReciprocalRankFusion,
)

vector = [
    {
        "content": "A",
        "metadata": {
            "chunk_id": "1"
        },
    },
    {
        "content": "B",
        "metadata": {
            "chunk_id": "2"
        },
    },
]

bm25 = [
    {
        "content": "B",
        "metadata": {
            "chunk_id": "2"
        },
    },
    {
        "content": "A",
        "metadata": {
            "chunk_id": "1"
        },
    },
]

results = ReciprocalRankFusion.fuse(
    vector,
    bm25,
)

for result in results:

    print(
        result["metadata"]["chunk_id"],
        result["rrf_score"],
    )