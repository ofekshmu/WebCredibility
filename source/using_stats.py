import pandas as pd
from Statistics import SeriesAnalysis
from tqdm import tqdm


def read_excel_and_analyze(filepath: str, column_names: list = None) -> None:
    """
    Read a table from an Excel file, iterate through its columns, and call the methods from the
    SeriesAnalysis class on each column.

    Args:
      filepath (str): The path to the Excel file to read the table from.

    Returns:
      None
    """
    print("Calculating statistics...")
    df = pd.read_excel(filepath)

    with open('statistics.txt', 'a') as f:

        f.write('column,mean,median,mode,std,var,correlation\n')

        if column_names is None:
            column_names = df.columns

        for col in tqdm(column_names):
            series = df[col]

            SeriesAnalysis.histogram(series)
            SeriesAnalysis.line_plot(series)
            SeriesAnalysis.scatter_plot(series)

            likert_corr = SeriesAnalysis.correlation(series, df['Likert rating'])
            stats = SeriesAnalysis.statistics(series)
            f.write(f'{col},{stats["mean"]},{stats["median"]},{stats["mode"]},\
                {stats["std"]},{stats["var"]},{likert_corr}\n')
