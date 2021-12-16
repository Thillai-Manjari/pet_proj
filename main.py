from fastapi import FastAPI
from Routes.Teachers import teacher

app = FastAPI()
app.include_router(teacher)