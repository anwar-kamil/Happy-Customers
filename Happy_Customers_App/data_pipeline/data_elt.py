import pandas as pd


class ExcelLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            df = pd.read_csv(self.file_path)
            return df
        except Exception as e:
            print(f"Error loading data from Excel: {e}")
            raise Exception("Could not ELT data in data_elt.py")
