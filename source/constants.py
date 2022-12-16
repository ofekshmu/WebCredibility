
class Constants:
    # Path to Excel holding url basic info and prediction
    DATA_PATH = "data/web_credibility_1000_url_ratings.xls"
    # Name of the output file (path and ending specified in code)
    OUTPUT_FILE_NAME = "result"
    # Headers for final, exported excel chart
    HEADERS = ["Original row ID",
               "URL",
               "Result Rank",
               "Links", "a tags",
               "Word count",
               "Misspelled words",
               "misspelled_percent (%)",
               "Char count",
               "Img count",
               "Banner count",
               "Likert Raiting"]
    CACHED_DATA_PATH = "data/Cached Pages"
    CREATED_DATA_PATH = "data/Created HTML"
    HTML_LOG = "data/Cached Pages/hts-cache/new.txt"
    KEY_WORD = "PagesForAllUrls"
    PATH_CONFIG = "path_config.json"

    # Flags
    CREATE_HTML_ON = True


def log(msg: str):
    print(msg)
    f = open("log.txt", 'a')
    f.write(f"{msg}\n")
