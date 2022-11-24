from typing import Union
from constants import log
from urllib.request import urlopen
from urllib.error import HTTPError

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
    def find_cached_html(url: str) -> Union[str, None]:
        """
        Look for the html with the specified url in the Cached pages folder,
        return the ralative path of the file if found, else, return None.
        """
        folder_names = [] # TODO
        for name in folder_names:
            if url.find(name) != -1:
                # if has a single html file -> return path to it.
                # if has more folders, repeat process again.

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
            with open( f"data\Created HTML\{idx}.html", 'w', encoding="utf-8", errors='ignore') as output:
                output.write(content)
            log(f"{idx} Success: Created file {idx}.html for url: {url}")
            return True

        except HTTPError as e:
            log(f"{idx} FAILED: Received an HTTPError for {idx} -> {url}")
            
        return False