from constants import log
from urllib.request import urlopen
from urllib.error import HTTPError
from constants import Constants
from bs4 import BeautifulSoup
from typing import Union


class HtmlParser:

    def __init__(self, path: str = None):
        """
        Initialize a new html file.
        """
        if path is not None:
            f = open(path, 'r')
            self.soup = BeautifulSoup(f.read(), 'html.parser')

    def set_new_page(self, path: str) -> bool:
        """
        TODO
        """
        try:
            f = open(f"data\{path}", 'r', encoding="utf8")
            self.soup = BeautifulSoup(f.read(), 'html.parser')
            return True
        except:
            log(f"File Does Not exist is the specified location!")
            return False

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
    def create_html(url: str, idx: int) -> Union[str, None]:
        """
        Try loading the Html file and downloading its content.
        returns the new location or None if operation failed
        """
        try:
            with urlopen(url) as webpage:
                content = webpage.read().decode("utf8")

            # Save to file.
            path = f"data\Created HTML\{idx}_Created.html"
            with open(path, 'w', encoding="utf-8", errors='ignore') as output:
                output.write(content)
            log(f"{idx} Success: Created file {idx}.html for url: {url}")
            return path.replace('/', '\\')

        except HTTPError as e:
            log(f"{idx} FAILED: Received an HTTPError for {idx} -> {url}")
        except Exception as e:
            log("Got some other error...")
            
        return None

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
            # First row of the files is the header row - skip it
            if idx == 0:
                continue

            if idx % int(1662*0.05) == 0:
                # print progress
                # file has a total of 1663 lines
                print(f"> > > > > > > > > > > > > > > > > Identifying locations {idx*100 // 1662}%")

            lst = line.split("\t")
            url = lst[-3]
            full_path = lst[-2]
            try:
                index = full_path.index(remote_folder) + len(remote_folder) 
            except:
                # Not all url have a location directory, we will skip those if the index function returns an error.
                print(f"line no' {idx}: Bad path in line {idx}")
                continue
            # Extract the relative path out of hte full path
            relative_path = f"Cached Pages\{full_path[index:]}"
            dict[url] = relative_path.replace('/', '\\')
        return dict
