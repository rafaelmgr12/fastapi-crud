from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}
