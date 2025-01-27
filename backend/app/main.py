from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"])

@app.get("/")
def ktips_root():
    return {"message": "Hello KTiPs Community!"}

@app.get("/api/data")
def get_data():
    return{"data": "This is data from FastAPI backend!"}
