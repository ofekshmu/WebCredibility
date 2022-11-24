from typing import Union
from constants import log
from urllib.request import urlopen
from urllib.error import HTTPError
from constants import Constants
import shutil

import os

class HtmlParser:

    
    def __init__(self, link: str):
        """
        Initialize a new html file.
        """
        self.html = link

    def set_new_page(self, link: str) -> None:
        pass

    def get_word_count(self) -> int:
        pass

    def get_mispelling_count(self) -> int:
        pass

    def get_banner_count(self) -> int:
        pass

    def get_ref_count(self) -> int:
        pass

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