
class Constants:
    # Path to Excel holding url basic info and prediction
    DATA_PATH = "data/web_credibility_1000_url_ratings.xls"
    EXPERT_RAITING_PATH = "data/web_credibility_expert_ratings_for_test_set.xlsx"
    # Name of the output file (path and ending specified in code)
    OUTPUT_FILE_NAME = "result"
    OUTPUT_EXPERT_NAME = "secondary"
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
               "Link depth",
               "Special characters",
               "Likert Raiting"]
    CACHED_DATA_PATH = "data/Cached Pages"
    CREATED_DATA_PATH = "data/Created HTML"
    HTML_LOG = "data/Cached Pages/hts-cache/new.txt"
    KEY_WORD = "PagesForAllUrls"
    PATH_CONFIG = "path_config.json"

    # Flags
    CREATE_HTML_ON = True
    MEMOIZATION = True
    MEMO_PATH = "Misspelled_data.json"

    TLD = ["com", "org", "net", "edu", "info", "biz", "io", "gov"]

    # Features for analisys
    FEATURES_FOR_ANALISYS_DEFAULT = ["Result Rank",
                                     "Links",
                                     "a tags",
                                     "Word count",
                                     "Misspelled words",
                                     "Img count"]
    FEATURES_FOR_ANALISYS_EXPERTS = ["Links",
                                     "a tags",
                                     "Word count",
                                     "Misspelled words",
                                     "Img count"]                               

def log(msg: str):
    print(msg)
    f = open("log.txt", 'a')
    f.write(f"{msg}\n")
