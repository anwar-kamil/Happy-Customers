from service import Service
import uvicorn
from fastapi import FastAPI, UploadFile


app = FastAPI()


@app.post("/api/classify")
async def classify(file: UploadFile):
    try:
        service = Service(file)
        data = await service.get_result()
        return True
    except Exception as e:
        return {"error": e}




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


