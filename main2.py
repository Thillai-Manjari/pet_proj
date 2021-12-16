from fastapi import FastAPI
from routes2.student import student

app = FastAPI()
app.include_router(student)