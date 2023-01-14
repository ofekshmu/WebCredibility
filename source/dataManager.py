from typing import List
import pandas as pd
from constants import Constants


class DataManger:

    def __init__(self, headers: List):
        """
        Create a pandas data frame with headers as its first row 
        """
        self.headers = headers
        self.table = pd.DataFrame(columns=headers)
        self.expert_raiting_table = pd.DataFrame(columns=headers + ["Rater Id"])

    def add_row(self, row, expert_raiting: bool) -> None:
        """
        Add a single row into the active table
        """
        if expert_raiting:
            self.table = pd.concat([self.expert_raiting_table,
                                   pd.Series(row).to_frame().T],
                                   ignore_index=True)
        else:
            self.table = pd.concat([self.table,
                                   pd.Series(row).to_frame().T],
                                   ignore_index=True)

    def export_table(self, expert_raiting: bool) -> None:
        """
        Export the data frame located in self.table as an excel file to
        the output directory.
        """
        if expert_raiting:
            self.table.to_excel(f"output/{Constants.OUTPUT_FILE_NAME}.xlsx", index=False)
        else:
            self.table.to_excel(f"output/{Constants.OUTPUT_EXPERT_NAMER}.xlsx", index=False)

    @staticmethod
    def read_table(expert_raiting: bool) -> List:
        """
        A function that returns the original excel table
        """
        if expert_raiting:
            return pd.read_excel(Constants.EXPERT_RAITING_PATH)
        else:
            return pd.read_excel(Constants.DATA_PATH)