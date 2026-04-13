from fastapi import FastAPI
import json 


app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello, World!"}

@app.get("/about")
def about():
    return {"message": "This is the about page."}

@app.get("/view")
def view():
    with open("sample.json", "r") as file:
        data = json.load(file)
    return {"data": data}