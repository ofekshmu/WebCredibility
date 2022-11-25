
class Constants:
    DATA_PATH = "data/web_credibility_1000_url_ratings.xls"
    OUTPUT_FILE_NAME = "result"
    HEADERS = ["ID", "Link", "Result rank", "Likert raiting"]
    CACHED_DATA_PATH = "data/Cached Pages"

    # Flags
    CREATE_HTML_ON = False


def log(msg: str):
    print(msg)
    f = open("log.txt", 'a')
    f.write(f"{msg}\n")