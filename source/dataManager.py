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
        self.original_table = pd.read_excel(Constants.DATA_PATH)


    def add_row(self, row) -> None:
        """
        Add a single row into the active table
        """
        self.table = pd.concat([self.table, pd.Series(row).to_frame().T], ignore_index=True)

    def export_table(self) -> None:
        """
        Export the data frame located in self.table as an excel file to
        the output directory.
        """
        print(self.table)
        self.table.to_excel(f"output/{Constants.OUTPUT_FILE_NAME}.xlsx", index=False)
    
    def read_table(self) -> List:
        """
        A function that returns the original excel table
        """
        return self.original_table

