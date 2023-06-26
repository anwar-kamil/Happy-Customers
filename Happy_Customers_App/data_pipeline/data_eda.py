from pandas_profiling import ProfileReport


class AutoEda:
    def __init__(self, data):
        self.data = data

    def get_eda(self):
        try:
            profile = ProfileReport(self.data, title="Happy Customers Report")
            profile.to_file(output_file='report.html')
            return profile
        except Exception as e:
            print(f"Error generating autoEDA html report: {e}")
            raise Exception("Could not ELT data in data_elt.py")