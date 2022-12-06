def main():
    pass


if __name__ == "__main__":
    main()

import pandas as pd
from Statistics import SeriesAnalysis


def read_excel_and_analyze(filepath: str) -> None:
    """
    Read a table from an Excel file, iterate through its columns, and call the methods from the
    SeriesAnalysis class on each column.

    Args:
      filepath (str): The path to the Excel file to read the table from.

    Returns:
      None
    """

    df = pd.read_excel(filepath)

    for col in df.columns:
        series = df[col]

        likert_corr = SeriesAnalysis.correlation(series, df['Likert rating'])

        SeriesAnalysis.histogram(series)
        SeriesAnalysis.line_plot(series)
        SeriesAnalysis.scatter_plot(series)
        stats = SeriesAnalysis.statistics(series)
