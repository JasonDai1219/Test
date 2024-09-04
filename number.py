import streamlit as st
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.wsgi import WSGIMiddleware

app = FastAPI()

class NumberResponse(BaseModel):
    number: int

# Create an API route
@app.get("/get_number", response_model=NumberResponse)
def get_number():
    generated_number = 42  # Replace with the actual generated number
    return {"number": generated_number}

# Mount the FastAPI app to Streamlit
st.write("Deployed Streamlit app with API")
st.write("Check `/get_number` to fetch the number")

st.experimental_get("get_number", WSGIMiddleware(app))  # This exposes your API while Streamlit is running
