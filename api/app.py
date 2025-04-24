from fastapi import FastAPI
from model.iris import PredictRequest, PredictResponse
from inference import SVMModel


app = FastAPI()

svm_model = SVMModel()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    iris_dict = {0: "Iris setosa", 1: "Iris versicolor", 2: "Iris virginica"}

    user_input_X = [list(request.model_dump().values())]

    prediction = svm_model.predict(user_input_X)

    return PredictResponse(prediction=iris_dict[prediction[0]])


# # START ME:
# uv run uvicorn app:app --reload --port=8000
