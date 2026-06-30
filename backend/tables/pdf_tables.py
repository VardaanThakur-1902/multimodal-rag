import pdfplumber
import pandas as pd

from schemas.table import TableData
from tables.markdown_converter import (
    MarkdownConverter,
)


class PDFTableExtractor:

    @staticmethod
    def extract(
        file_path: str,
    ) -> list[TableData]:

        extracted_tables = []

        with pdfplumber.open(file_path) as pdf:

            for page_number, page in enumerate(pdf.pages):

                tables = page.extract_tables()

                if not tables:
                    continue

                for index, table in enumerate(tables):

                    if not table:
                        continue

                    dataframe = pd.DataFrame(table)

                    dataframe.columns = dataframe.iloc[0]

                    dataframe = dataframe.iloc[1:]

                    markdown = (
                        MarkdownConverter
                        .dataframe_to_markdown(
                            dataframe
                        )
                    )

                    extracted_tables.append(

                        TableData(
                            page_number=page_number + 1,
                            table_index=index + 1,
                            markdown=markdown,
                            rows=len(dataframe),
                            columns=len(dataframe.columns),
                        )

                    )

        return extracted_tables