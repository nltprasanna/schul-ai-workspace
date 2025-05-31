from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from AI service!"}

@app.get("/predict")
def predict():
    return {"result": "This is a dummy AI response"}