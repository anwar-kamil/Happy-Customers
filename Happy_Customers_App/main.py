from fastapi import FastAPI
from data_pipeline.data_elt import ExcelLoader
from data_pipeline.data_eda import AutoEda
import uvicorn


app = FastAPI()


@app.post("/xgboost")
async def root():
    try:
        loader = ExcelLoader('ACME-HappinessSurvey2020.csv')
        data = ExcelLoader.load_data(loader)
        eda_obj = AutoEda(data)
        eda_obj.get_eda()
    except Exception as e:
        return {"error": e}




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


