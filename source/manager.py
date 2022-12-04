from dataManager import DataManger
from constants import Constants
from htmlParser import HtmlParser
from constants import log
import json
from os import listdir


class Manager:

    def __init__(self):

        self.parser = HtmlParser()
        self.dataManager = DataManger(Constants.HEADERS)

        try:
            json_file = open(Constants.PATH_CONFIG, "r")
            log("Found path_config file!")
        except:
            log("path_config file not found, creating...")
            self.__search_and_write()
            json_file = open(Constants.PATH_CONFIG, "r")
        self.paths = json.load(json_file)

    def __search_and_write(self) -> None:
        """
        The function creates
        The function will identify the location of each file with the url specified in the xlsx file.
        The relative path found will be written to XXX.txt.
        if path was not found, function will try and create it by downloading the information.
        """

        log("Extracting information from given log file...")
        dict = HtmlParser.extract_logs()
        log("Looking for existing HTML files...")
        table = DataManger.read_table()
        total = len(table)
        url_lst = table["URL"]

        for idx, url in enumerate(url_lst, start=2):
            if (idx - 1) % (total // 0.05) == 0:
                print(f"Current progress: {(idx-1)*100/total}%")

            if url not in dict.keys():
                log(f"URL not found in cached folders, trying to download...")
                path = HtmlParser.create_html(url, idx)
                dict[url] = f"Created HTML\{path}"
                continue

        with open(Constants.PATH_CONFIG, "w") as outfile:
            json.dump(dict, outfile)

    def parse_and_export(self) -> None:
        table = DataManger.read_table()
        url_lst = table["URL"]
        length = len(url_lst)
        log(f"Adding new data to result.csv...")
        for idx, url in enumerate(url_lst, start=1):
            if idx % (length*0.01) == 0:
                log(f"Progress: {idx * 100//length}%")
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
                          x["Likert Rating"]]
                row = dict(zip(Constants.HEADERS, values))
                self.dataManager.add_row(row)
        self.dataManager.export_table()
