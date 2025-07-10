from fastapi import FastAPI

app = FastAPI(
    title =  "Welcome to NoteAPI", 
    description = "A RESTful API (or web API) that lets users create, read, update, and delete (CRUD) notes through HTTP requests."
)

@app.get("/")
def read_notes():
    return{"Message": "Read Notes"}

@app.post("/")
def add_notes():
    return{"Message": "Add Notes"}

@app.put("/")
def update_notes():
    return{"Message": "Update Notes"}

@app.delete("/")
def delete_notes():
    return{"Message": "Delete Notes"}