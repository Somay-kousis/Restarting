from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is running"}

# / path

@app.get("/hello/{name}")
def greet(name: str):
    return {"message": f"Hello {name}"}

# /hello/Blink

@app.get("/search")
def search(city: str):
    return {"city": city}

@app.post("/student")
def add_student(student: dict):
    name = student["name"]
    marks = student["marks"]

    return {
        "message": f"Student {name} added",
        "marks": marks
    }
# ?city=Delhi query parameteer 

@app.get("/quote")
def get_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = response.json()

    return {
        "quote": data["content"],
        "author": data["author"]
    }

@app.get("/motivation")
def motivation(topic: str):
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = response.json()

    return {
        "topic": topic,
        "quote": data["content"],
        "author": data["author"]
    }

# GET  → ask for data
# POST → send data

