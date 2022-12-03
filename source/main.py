from manager import Manager
from constants import log
from datetime import datetime


def main():
    log(f"{50*'~'}\nStarting Run...\n Date is {datetime.now()}\n{50*'~'}")
    m = Manager()
    m.create_HTML_files()
    m.start_parsing()


if __name__ == "__main__":
    main()