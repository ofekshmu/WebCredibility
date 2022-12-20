from manager import Manager
from constants import log
from datetime import datetime


def main():
    log(f"{50*'~'}\nStarting Run...\n Date is {datetime.now()}\n{50*'~'}")
    myManager = Manager()
    myManager.parse_and_export()
    myManager.read_excel_and_analyze(["Result Rank", "Links", "a tags", "Word count", "Misspelled words", "Img count"])
    log(f"{50*'~'}\nEnded Successfully!\n Date is {datetime.now()}\n{50*'~'}")


if __name__ == "__main__":
    main()
