from constants import log
from urllib.request import urlopen
from urllib.error import HTTPError
from constants import Constants
from bs4 import BeautifulSoup
import os


class HtmlParser:

    def __init__(self, file_name: str):
        """
        Initialize a new html file.
        """
        f = open(f"data\Created HTML\{file_name}", 'r')
        self.soup = BeautifulSoup(f.read(), 'html.parser')

    def set_new_page(self, file_name: str) -> None:
        """
        TODO
        """
        f = open(f"data\Created HTML\{file_name}", 'r', encoding="utf8")
        self.soup = BeautifulSoup(f.read(), 'html.parser')

    def get_word_count(self) -> int:
        pass

    def get_mispelling_count(self) -> int:
        from textblob import Word

        def check_spelling(word):
            
            word = Word(word)
            result = word.spellcheck()
            
            if word == result[0][0]:
                return True
            return False

        text = self.soup.get_text()
        word_lst = text.replace('\n', ' ').replace(', ', ' ').split()

        count = 0
        print(len(word_lst))
        for element in word_lst:
            if check_spelling(element):
                count += 1
        print(len(word_lst))
        print(count)
        return count
        
    def get_banner_count(self) -> int:
        pass

    def get_link_count(self) -> int:
        """
        Returns the total number of links and a elements in the selected html file.
        """
        link_count = len(self.soup.find_all('link'))
        a_count =   len(self.soup.find_all('a'))
        return link_count + a_count


    @staticmethod
    def create_html(url: str, idx: int) -> bool:
        """
        Try loading the Html file and downloading its content.
        returns True uppon successful downdload and false otherwise.
        """
        try:
            with urlopen(url) as webpage:
                content = webpage.read().decode("utf8")

            # Save to file.
            with open( f"data\Created HTML\{idx}_Created.html", 'w', encoding="utf-8", errors='ignore') as output:
                output.write(content)
            log(f"{idx} Success: Created file {idx}.html for url: {url}")
            return True

        except HTTPError as e:
            log(f"{idx} FAILED: Received an HTTPError for {idx} -> {url}")
        except Exception as e:
            log("Got some other error...")
            
        return False

    @staticmethod
    def extract_logs() -> bool:
        """
        Extract the path location of all files with urls correpsonding to the given excel.
        return a dictionary with url as keys and relative path as a value.
        """
        dict = {}
        file = open(Constants.HTML_LOG, 'r', encoding="windows-1252")
        remote_folder = "PagesForAllUrls/"
        for idx, line in enumerate(file):
            if idx == 0: # First row of the files is the header row - skip it
                continue
            # file has a total of 1663 lines
            print(f"Identifying locations {idx}/1662", end="")
            lst = line.split("\t")
            url = lst[-3]
            full_path = lst[-2]
            try:
                index = full_path.index(remote_folder) + len(remote_folder) 
            except:
                # Not all url have a location directory, we will skip those if the index function returns an error.
                print(f" X - Bad path")
                continue
            # Extract the relative path out of hte full path
            relative_path = full_path[index:]
            dict[url] = [relative_path]
            print(f" V - Inserted")
        return dict
