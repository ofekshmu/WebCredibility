import matplotlib.pyplot as plt
import pandas as pd


class SeriesAnalysis:
    """
    A class for performing various data analysis tasks on a `pandas.Series` object.
    """

    @staticmethod
    def histogram(series: pd.Series, name: str) -> None:
        """
        Create an histogram for the given series and save it as an image in the current directory.

        Args:
          series (pandas.Series): The `pandas.Series` object to create the histogram for.

        Returns:
          None
        """
        # Plot the histogram
        series.plot.hist()

        # Save the histogram as an image in the current directory
        plt.savefig(f'histogram_{name}.png')

    @staticmethod
    def line_plot(series: pd.Series, name: str) -> None:
        """
        Create a line plot for the given series and save it as an image in the current directory.

        Args:
          series (pandas.Series): The `pandas.Series` object to create the line plot for.

        Returns:
          None
        """
        # Plot the line graph
        series.plot.line()

        # Save the line graph as an image in the current directory
        plt.savefig(f'line_plot_{name}.png')

    @staticmethod
    def scatter_plot(series: pd.Series, name: str) -> None:
        """
        Create a scatter plot for the given series and save it as an image in the current directory.

        Args:
          series (pandas.Series): The `pandas.Series` object to create the scatter plot for.

        Returns:
          None
        """
        # Plot the scatter plot
        series.plot.scatter()

        # Save the scatter plot as an image in the current directory
        plt.savefig(f'scatter_plot_{name}.png')

    @staticmethod
    def correlation(series1: pd.Series, series2: pd.Series) -> float:
        """
        Calculate the correlation between the two given series.

        Args:
          series1 (pandas.Series): The first `pandas.Series` object to calculate the correlation for.
          series2 (pandas.Series): The second `pandas.Series` object to calculate the correlation for.

        Returns:
          float: The correlation between the two series.
        """
        return round(series1.corr(series2), 3)

    @staticmethod
    def statistics(series: pd.Series) -> pd.Series:
        """
        Calculate the mean, median, mode, standard deviation, and variance of the given series and
        return them in a `pandas.Series` object.

        Args:
          series (pandas.Series): The `pandas.Series` object to calculate the statistical values for.

        Returns:
          pandas.Series: A `pandas.Series` object containing the calculated statistical values.
        """
        # Calculate the statistical values
        mean = round(series.mean(), 2)
        median = round(series.median(), 2)
        mode = series.mode()
        std = round(series.std(), 2)
        var = round(series.var(), 2)

        # Create a pandas.Series object to hold the results
        stats = pd.Series(
            data=[mean, median, mode, std, var],
            index=['mean', 'median', 'mode', 'std', 'var'],
        )

        # Return the pandas.Series object
        return stats
