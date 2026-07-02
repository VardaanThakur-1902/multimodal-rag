from query_rewriting.query_rewriter import (
    QueryRewriter,
)


def main():

    history = [

        {
            "role": "user",
            "content": "What is Python?"
        },

        {
            "role": "assistant",
            "content": "Python is a programming language."
        }

    ]

    rewritten = QueryRewriter.rewrite(

        "Who created it?",

        history,

    )

    print("=" * 60)
    print("REWRITTEN QUESTION")
    print("=" * 60)
    print(rewritten)


if __name__ == "__main__":
    main()