from urllib.request import urlopen
from urllib.error import HTTPError
from dataManager import DataManger
from constants import Constants

def log(msg: str):
    print(msg)
    f = open("log.txt", 'a')
    f.write(f"{msg}\n")


class Manager:

    def __init__(self):
        # self.parser = HtmlParser()
        self.dataManager = DataManger(Constants.HEADERS)

    def create_HTML_files(self):
        table = DataManger.read_table(Constants.DATA_PATH)
        total = len(table)
        url_lst = table["URL"]
        for idx, url in enumerate(url_lst, start=2):
            print(f"Current progress: {idx-1}/{total}")
            # Download from URL and decode as UTF-8 text.
            try:
                with urlopen(url) as webpage:
                    content = webpage.read().decode("utf8")
            except HTTPError as e:
                log(f"File with URL {url} and index {idx} has resulted in error: {e}")
                continue

            # # Save to file.
            with open( f"data\Created HTML\{idx}.html", 'w', encoding="utf-8", errors='ignore') as output:
                output.write(content)




