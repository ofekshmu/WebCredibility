from manager import Manager
from constants import log, Constants
from datetime import datetime


def main():
    log(f"{50*'~'}\nStarting Run...\n Date is {datetime.now()}\n{50*'~'}")
    myManager = Manager()

    # ----------------- Execute the loop for the basic excel ----------------
    myManager.parse_and_export()
    myManager.read_excel_and_analyze(Constants.FEATURES_FOR_ANALISYS)
    # -------------------------------------------------------------------------

    # ----------------- Execute the loop for the experts table ----------------
    myManager.parse_and_export(expert_raiting=True)
    myManager.read_excel_and_analyze(Constants.FEATURES_FOR_ANALISYS_EXPERTS,
                                     expert_raiting=True)
    # -------------------------------------------------------------------------
    log(f"{50*'~'}\nEnded Successfully!\n Date is {datetime.now()}\n{50*'~'}")


if __name__ == "__main__":
    main()
