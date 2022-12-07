from dataManager import DataManger
from constants import Constants
from htmlParser import HtmlParser
from constants import log
import json
from tqdm import tqdm


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
                values = [idx,
                          x["URL"],
                          x["Result Rank"],
                          self.parser.get_link_count(),
                          "X",
                          self.parser.get_word_count(),
                          self.parser.is_url_contained_key_word(),
                          self.parser.get_char_count(),
                          self.parser.get_img_count(),
                          x["Likert Rating"]]
                row = dict(zip(Constants.HEADERS, values))
                self.dataManager.add_row(row)
        self.dataManager.export_table()
