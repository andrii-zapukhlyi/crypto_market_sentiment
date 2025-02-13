from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import tensorflow as tf
from tensorflow import keras
from pydantic import BaseModel
import pickle, re
from fastapi.middleware.cors import CORSMiddleware

with open('encoding_vars.pkl', 'rb') as f:
    my_data = pickle.load(f)

exec(my_data['clean_text'])
tokenizer = my_data["tokenizer"]
le = my_data["label_encoder"]
max_length = my_data["max_len"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

model = tf.keras.models.load_model("model.keras")

class InputData(BaseModel):
    data: str

@app.get("/", response_class=FileResponse)
async def serve_home():
    return "index.html"

@app.post("/predict")
async def predict(input_data: InputData):
    text = clean_text(input_data.data) # type: ignore
    tokenized = tokenizer.texts_to_sequences([text])
    padded = keras.preprocessing.sequence.pad_sequences(tokenized, maxlen=max_length, padding="post")
    prediction = model.predict(padded, verbose=0).argmax(axis=1)
    return {"prediction": le.inverse_transform(prediction).item()}