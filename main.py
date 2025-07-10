from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_notes():
    return{"Message": "Read Notes"}

@app.post("/")
def read_notes():
    return{"Message": "Add Notes"}

@app.put("/")
def read_notes():
    return{"Message": "Update Notes"}

@app.delete("/")
def read_notes():
    return{"Message": "Delete Notes"}