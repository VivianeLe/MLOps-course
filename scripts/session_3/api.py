from enum import Enum
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from router import predict, utils, calculation
from schemas import request, response
import mlflow.sklearn
import pandas as pd

app = FastAPI()
app.include_router(predict.housing_router)
app.include_router(calculation.calculation_router)
# app.include_router(utils.utils_router)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}



# model_name = "housing_price_predictor"
# model_version = "1"
# alias = "the_best"
# mlflow.set_tracking_uri(uri="http://localhost:8080")
# # model_uri = f"models:/{model_name}/{model_version}"
# model_uri = f"models:/{model_name}@{alias}"
# model = mlflow.sklearn.load_model(model_uri)

# @app.post("/predict", response_model=response.HousingPredictionResponse)
# def predict(request:request.HousingPredictionRequest) -> response.HousingPredictionResponse:
#     data = {
#         "Avg. Area Income": [request.average_area_income],
#         "Avg. Area House Age": [request.average_area_house_age],
#         "Avg. Area Number of Rooms": [request.average_area_number_of_rooms],
#         "Avg. Area Number of Bedrooms": [request.average_area_number_of_bedrooms],
#         "Area Population": [request.area_population],
#     }
#     df = pd.DataFrame(data)
#     predictions = model.predict(df)
#     return response.HousingPredictionResponse(predicted_price = predictions[0])

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=3000, reload=True)