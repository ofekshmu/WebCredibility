from typing import List
import pandas as pd
from constants import Constants

class DataManger:

    def __init__(self, headers: List):
        """
        Create a pandas data frame with headers as its first row 
        """
        self.table = pd.DataFrame(columns=headers)

    def add_row(self) -> None:
        """
        Add a single row into the active table
        """
        pass

    def export_table(self) -> None:
        """
        Export the data frame located in self.table as an excel file to
        the output directory.
        """
        self.table.to_excel(f"output/{Constants.OUTPUT_FILE_NAME}", index=False)
    
    @staticmethod
    def read_table(self, path: str) -> List:
        """
        A static function to read an excel file into a data frame.
        """
        pass

