from manager import Manager
from constants import log
from datetime import datetime


def main():
    log(f"{50*'~'}\nStarting Run...\n Date is {datetime.now()}\n{50*'~'}")
    myManager = Manager()
    # m.establish_path()
    # m.start_parsing()


if __name__ == "__main__":
    main()