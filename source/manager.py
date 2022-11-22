from urllib.request import urlopen
from htmlParser import HtmlParser
from dataManager import DataManger
from constants import Constants

class Manager:

    def __init__(self):
        self.parser = HtmlParser()
        self.dataManager = DataManger(Constants.HEADERS)

    def create_HTML_files(self):
        table = DataManger.read_table(Constants.DATA_PATH)
        for idx, row in enumerate(table, start=2):
            link = row[3]
            # Download from URL and decode as UTF-8 text.
            with urlopen(link) as webpage:
                content = webpage.read().decode()

            # # Save to file.
            with open( f"{idx}.html", 'w' ) as output:
                output.write( content )