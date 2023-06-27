import pandas as pd
import io


class ExcelLoader:
    def __init__(self, file):
        self.file = file

    async def load_data(self):
        try:
            contents = await self.file.read()
            file_obj = io.BytesIO(contents)
            df = pd.read_csv(file_obj)
            return df
        except Exception as e:
            print(f"Error loading data from Excel: {e}")
            raise Exception("Could not ELT data in data_elt.py")
