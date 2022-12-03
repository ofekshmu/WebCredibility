from dataManager import DataManger
from constants import Constants
from htmlParser import HtmlParser
from constants import log
from os import listdir


class Manager:

    def __init__(self):
        file_name = "961_Created.html"

        self.parser = HtmlParser(file_name)
        self.dataManager = DataManger(Constants.HEADERS)

    def create_HTML_files(self) -> None:
        if Constants.CREATE_HTML_ON:
            log("Creating Html files...")
            table = DataManger.read_table()
            total = len(table)
            url_lst = table["URL"]

            dict = HtmlParser.extract_logs()

            for idx, url in enumerate(url_lst, start=2):
                print(f"Current progress: {idx-1}/{total}")

                if url in dict.keys():
                    # idx idicate row number in the Constants.DATA_PATH
                    temp = dict[url]
                    dict[url] = temp.append(idx)
                    log(f"Found url in cached folder")
                    continue

                if HtmlParser.create_html(url, idx):
                    # add page link to dictionary?
                    continue
        else:
            log(f"Skipping HTML creation")

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