from fastapi import FastAPI, File, UploadFile
from pathlib import Path
from zoo_animals import AnimalClassifier

app = FastAPI()

model_path = Path()/"zoo_animals.pkl"
zaclass = AnimalClassifier(model_path)

@app.post("/animal/")
def define(file: UploadFile = File(...)):
    return zaclass.predict(file.file)