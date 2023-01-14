from typing import List
import pandas as pd
from constants import Constants


class DataManger:

    def __init__(self):
        """
        Create a pandas data frame with headers as its first row
        """
        self.table = pd.DataFrame(columns=self.__build_headers())
        self.expert_raiting_table = pd.DataFrame(columns=self.__build_headers(True))

    def add_row(self, values, expert_raiting: bool = False) -> None:
        """
        Add a single row into the active table
        """
        row = dict(zip(self.__build_headers(expert_raiting), values))
        if expert_raiting:
            self.expert_raiting_table = pd.concat([self.expert_raiting_table,
                                        pd.Series(row).to_frame().T],
                                        ignore_index=True)
        else:
            self.table = pd.concat([self.table,
                                   pd.Series(row).to_frame().T],
                                   ignore_index=True)

    def export_table(self, expert_raiting: bool = False) -> None:
        """
        Export the data frame located in self.table as an excel file to
        the output directory.
        """
        if expert_raiting:
            self.expert_raiting_table.to_excel(f"output/{Constants.OUTPUT_EXPERT_NAME}.xlsx", index=False)
        else:
            self.table.to_excel(f"output/{Constants.OUTPUT_FILE_NAME}.xlsx", index=False)

    @staticmethod
    def read_table(expert_raiting: bool = False) -> List:
        """
        A function that returns the original excel table
        """
        if expert_raiting:
            return pd.read_excel(Constants.EXPERT_RAITING_PATH)
        else:
            return pd.read_excel(Constants.DATA_PATH)

    def __build_headers(self, expert_raiting: bool = False):
        base = Constants.HEADERS[:-1] + Constants.TLD + [Constants.HEADERS[-1]]
        if expert_raiting:
            base.remove("Result Rank")
            base.append("Rater ID")
        return base
