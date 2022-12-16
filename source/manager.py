from dataManager import DataManger
from constants import Constants
from htmlParser import HtmlParser
from constants import log
import json
from tqdm import tqdm
import pandas as pd
from Statistics import SeriesAnalysis


class Manager:

    def __init__(self):

        self.parser = HtmlParser()
        self.dataManager = DataManger(Constants.HEADERS)

        try:
            json_file = open(Constants.PATH_CONFIG, "r")
            log("Found path_config file!")
        except FileNotFoundError:
            log("path_config file not found, creating...")
            self.__search_and_write()
            json_file = open(Constants.PATH_CONFIG, "r")
        self.paths = json.load(json_file)

    def __search_and_write(self) -> None:
        """
        The function creates a json file indicating the relation between the url and its relative directory.
        if the html file does not exist in the dictionary returned by_extract_logs, the function will try to
        create the file manualy.
        """

        log("Extracting information from given log file...")
        dict = HtmlParser.extract_logs()
        log("Looking for existing HTML files...")
        table = DataManger.read_table()
        total = len(table)
        url_lst = table["URL"]

        for idx, url in tqdm(enumerate(url_lst, start=2), total=len(url_lst)):

            if url not in dict.keys():
                log(f"URL not found in cached folders, trying to download...")
                path = HtmlParser.create_html(url, idx)
                dict[url] = f"Created HTML\{path}"
                continue

        with open(Constants.PATH_CONFIG, "w") as outfile:
            json.dump(dict, outfile)

    def parse_and_export(self) -> None:
        """
        The function will iterate over all existing html, parse and create an xlsx
        file containing the results gathered.
        """
        table = DataManger.read_table()
        url_lst = table["URL"]
        length = len(url_lst)
        log(f"Adding new data to result.csv...")
        for idx, url in tqdm(enumerate(url_lst, start=1), total=len(url_lst)):
            
            if url in self.paths.keys():
                path = self.paths[url]
                if not self.parser.set_new_page(path):
                    continue
                
                x = table.iloc[idx - 1]
                total_words = self.parser.get_word_count()
                misspelled_words = self.parser.get_mispelling_count()
                misspelled_percent = misspelled_words*100/total_words
                values = [idx,
                          x["URL"],
                          x["Result Rank"],
                          self.parser.get_link_count(),
                          self.parser.get_atag_count(),
                          total_words,
                          misspelled_words,
                          misspelled_percent,
                          self.parser.get_char_count(),
                          self.parser.get_img_count(),
                          self.parser.get_banner_count(),
                          x["Likert Rating"]]
                row = dict(zip(Constants.HEADERS, values))
                self.dataManager.add_row(row)
        self.dataManager.export_table()

    def read_excel_and_analyze(self, column_names: list = None) -> None:
        """
        Read a table from an Excel file, iterate through its columns, and call the methods from the
        SeriesAnalysis class on each column.

        Args:
        filepath (str): The path to the Excel file to read the table from.

        Returns:
        None
        """
        print("Calculating statistics...")
        df = pd.read_excel(f"output/{Constants.OUTPUT_FILE_NAME}.xlsx")

        with open('output/statistics/statistics.txt', 'w') as f:

            f.write(f'column\t\t\tmean\t\tmedian\t\tstd\t\t\tvar\t\t\tcorrelation\n')

            if column_names is None:
                column_names = df.columns

            for col in tqdm(column_names):
                series = df[col]

                SeriesAnalysis.histogram(series, col)
                # SeriesAnalysis.line_plot(series, col)
                SeriesAnalysis.scatter_plot(df['Likert Raiting'], series, col)

                likert_corr = SeriesAnalysis.correlation(series, df['Likert Raiting'])
                stats = SeriesAnalysis.statistics(series)
                f.write(f'{col}\t\t{stats["mean"]}\t\t{stats["median"]}\t\t{stats["std"]}\t\t{stats["var"]}\t\t{likert_corr}\n')
