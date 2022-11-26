from typing import Union
from constants import log
from urllib.request import urlopen
from urllib.error import HTTPError
from constants import Constants
import shutil
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
    def find_cached_html(url: str, idx: int) -> bool:
        """
        Look for the html with the specified url in the Cached pages folder.
        If found, copy to specified directory and return True, else return False.
        """
        def find_file(path: str, url: str) -> str:
            if os.path.isfile(path):
                return path

            folder_names = [] # Get all folder names in path
            for name in folder_names:
                if url.find(name) != -1:
                    return find_file(path + name, url)
            
            return None


        path = find_file(Constants.CACHED_DATA_PATH, url)
        if path is not None:
            original = path
            target = "data/Created HTML/{idx}_Cached.html"
            shutil.copyfile(original, target)
            return True
        return False

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