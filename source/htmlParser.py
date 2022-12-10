from constants import log
from urllib.request import urlopen
from urllib.error import HTTPError
from constants import Constants
from bs4 import BeautifulSoup
from typing import Union
from tqdm import tqdm


class HtmlParser:

    def __init__(self, path: str = None):
        """
        Initialize a new html file.
        """
        self.word_lst = []
        if path is not None:
            self.path = path
            with open(path, 'r') as file:
                self.soup = BeautifulSoup(file, 'html.parser')

    def set_new_page(self, path: str) -> bool:
        """
        TODO
        """
        try:
            self.path = path
            f = open(f"data\{path}", 'r', encoding="utf8")
            self.soup = BeautifulSoup(f.read(), 'html.parser')
            self.word_lst = []
            return True
        except Exception:
            # log(f"File Does Not exist is the specified location!")
            return False

    def get_word_count(self) -> int:
        """ T"""
        text = self.soup.get_text()
        word_lst = text.replace('\n', ' ').replace(', ', ' ').split()
        self.word_lst = [word for word in word_lst if word.isalpha() and len(word) > 1]
        return len(self.word_lst)

    def get_char_count(self) -> int:
        return len(self.soup.get_text())

    def get_img_count(self) -> int:
        return len(self.soup.find_all('img'))

    def is_url_contained_key_word(self) -> int:
        """
        TODO: bad functionality
        """
        lst = [".org.", ".wiki.", ".gov.", ".ac."]
        for word in lst:
            if word in self.path:
                return True
        return False

    def get_mispelling_count(self) -> int:
        """
        Get the number of misspelled words in the html.
        Make sure to call 'get_word_caount' before this function in order
        to initialize the word list of the html.
        """
        from textblob import Word

        def check_spelling(word):

            word = Word(word)
            result = word.spellcheck()

            if word == result[0][0]:
                return True
            return False

        if self.word_lst == []:
            raise Exception("self.word_lst is Empty! Please call 'get_Word_count' first!")

        count = 0
        for element in self.word_lst:
            if not check_spelling(element):
                count += 1
        return count

    def get_banner_count(self) -> int:
        pass

    def get_link_count(self) -> int:
        """
        Returns the total number of links and a elements in the selected html file.
        """
        link_count = len(self.soup.find_all('link'))
        a_count = len(self.soup.find_all('a'))
        return link_count + a_count

    # TODO make sure if this function corresponds with the stats of the provided html
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
        log("Extracting logs...")
        for idx, line in tqdm(enumerate(file)):
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
