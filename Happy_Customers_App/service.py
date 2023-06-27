from data_pipeline.data_eda import AutoEda
from data_pipeline.data_elt import ExcelLoader


class Service:
    def __init__(self, file):
        self.file = file

    async def get_result(self):
        try:
            loader = ExcelLoader(self.file)
            data = await ExcelLoader.load_data(loader)
            #eda_obj = AutoEda(data)
            #eda_obj.get_eda()
            return data
        except Exception as e:
            print(f"Error generating autoEDA html report: {e}")
            raise Exception("Could not ELT data in data_elt.py")









