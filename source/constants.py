
class Constants:
    DATA_PATH = "data/web_credibility_1000_url_ratings.xls"
    OUTPUT_FILE_NAME = "result"
    HEADERS = ["original_row_ID", "URL", "Result Rank", "embedded links", "Misspelled words", "Likert Raiting"]
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