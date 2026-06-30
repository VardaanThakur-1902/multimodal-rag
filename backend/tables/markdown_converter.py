import pandas as pd


class MarkdownConverter:

    @staticmethod
    def dataframe_to_markdown(
        dataframe: pd.DataFrame,
    ) -> str:

        dataframe = dataframe.fillna("")

        return dataframe.to_markdown(
            index=False
        )