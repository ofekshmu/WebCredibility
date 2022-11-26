from typing import List
import pandas as pd
from constants import Constants

class DataManger:

    def __init__(self, headers: List):
        """
        Create a pandas data frame with headers as its first row 
        """
        self.table = pd.DataFrame(columns=headers)
        print(self.table)


    def add_row(self, row) -> None:
        """
        Add a single row into the active table
        """
        self.table = pd.concat([self.table, row])

    def export_table(self) -> None:
        """
        Export the data frame located in self.table as an excel file to
        the output directory.
        """
        print(self.table)
        self.table.to_excel(f"output/{Constants.OUTPUT_FILE_NAME}.xlsx", index=False)
    
    @staticmethod
    def read_table(path: str) -> List:
        """
        A static function to read an excel file into a data frame.
        """
        return pd.read_excel(Constants.DATA_PATH)

