from dataManager import DataManger
from constants import Constants
from htmlParser import HtmlParser
from constants import log

class Manager:

    def __init__(self):
        # self.parser = HtmlParser()
        self.dataManager = DataManger(Constants.HEADERS)
        

    def create_HTML_files(self) -> None:
        if Constants.CREATE_HTML_ON:
            log("Creating Html files...")
            table = DataManger.read_table(Constants.DATA_PATH)
            total = len(table)
            url_lst = table["URL"]
            for idx, url in enumerate(url_lst, start=2):
                print(f"Current progress: {idx-1}/{total}")
                if HtmlParser.find_cached_html(url, idx):
                    continue
                if HtmlParser.create_html(url, idx):
                    continue
        else:
            log(f"Skipping HTML creation")

    def start_parsing(self) -> None:
        file_name = "961_Created.html"
        row_id = int(file_name.split("_")[0])
        given_table = DataManger.read_table(Constants.DATA_PATH)
        row = given_table.iloc[row_id]
        print(row)
        self.dataManager.add_row(row)
        self.dataManager.export_table()
        html_parser = HtmlParser(file_name)
        row = []
        row.append(html_parser.get_link_count())
        row.append(html_parser.get_mispelling_count())
