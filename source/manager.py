from dataManager import DataManger
from constants import Constants
from htmlParser import HtmlParser
from constants import log
import sys
import json
from os import listdir


class Manager:

    def __init__(self):
        file_name = "961_Created.html"

        self.parser = HtmlParser(file_name)
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
            print(f"Current progress: {idx-1}/{total}")

            if url in dict.keys():
                # idx idicate row number in the Constants.DATA_PATH
                log(f"Found url in cached folder")
            else:
                path = HtmlParser.create_html(url, idx)
                dict[url] = path
                continue

        with open(Constants.PATH_CONFIG, "w") as outfile:
            json.dump(dict, outfile)

    def start_parsing(self) -> None:
        name_lst = listdir(Constants.CREATED_DATA_PATH)
        length = len(name_lst)
        given_table = self.dataManager.read_table()
        offset = 2
        for idx, file_name in enumerate(name_lst, start=1):
            log(f"Adding new data to result.csv {idx}/{length} ")
            self.parser.set_new_page(file_name)
            row_id = int(file_name.split("_")[0])

            x = given_table.iloc[row_id - offset]
            values = [row_id,
                      x["URL"],
                      x["Result Rank"],
                      self.parser.get_link_count(),
                      "X",
                      x["Likert Rating"]]
            row = dict(zip(Constants.HEADERS, values))
            self.dataManager.add_row(row)
        self.dataManager.export_table()