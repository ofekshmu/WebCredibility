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
        html_parser = HtmlParser("961_Created.html")
        link_count = html_parser.get_link_count()
        mis_word_count = html_parser.get_mispelling_count()
