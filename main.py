#importing necessary modules
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#assigning note_id variable with a initial value of 1
note_id = 1
notes = {}#variable for storing the notes

#creating an app fastapi with title and description
app = FastAPI(
    title="Welcome to NoteAPI",
    description="A RESTful API (or web API) that lets users create, read, update, and delete (CRUD) notes through HTTP requests."
)
#Defining a Pydantic Model here. PydanticModel is like "When someone sends a note to me, it must have a title and content compulsary". If any one of these is not provided or they are of wrongtype, fastapi rejects it automatically.
class Notes(BaseModel):
    title: str
    content: str


#Creating a post method here. Post method lets user create their notes.
@app.post("/notes/")
#here, i have defined a function called add_notes with the parameters as pydantic model.
def add_notes(note: Notes):
    global note_id#note_id is declared outside so mentioning it is a global variable.
    notes[note_id] = note#this saves the note in your directory using note_id as the key.
    note_id += 1 #After saving,increasing the value of note_id by one for each new notes created lated on.
    #In fastapi, returning python dict means fastapi turns it automatically into json format.
    #Above, we have increased the value of note_is by 1 but this is the old note_id, so it is written to get the correct note_id.
    return {"id": note_id - 1, **note.dict()}
    #here, note.dict means note is a pydantic model so .dict changes it into a dictionary. fastapi needs a normal dict to turn it to JSON and ** is used to unpack the dictionary.




#Creating a get method here. It returns all the notes.
@app.get("/notes/")
def return_notes():
    #here, i have created a variable to store all notes with the id
    all_notes = []
     #looping through the notes dict
    for id, note in notes.items():
        #note_data is a temp variable to store the data
        note_data = {"id": id, **note.dict()}
        #adding the data to the all_notes list
        all_notes.append(note_data)
    return all_notes



#Creating a get method for returning the notes based on their id's.
@app.get("/notes/{note_id}")
#defining a function with argument as note_id as type int
def return_notes_id(note_id: int):
    #Here, if note_is is in notes list, 
    if note_id in notes:#here, if note_id is in notes:
        note = notes[note_id]#If it does exist, it says get that note from the dictionary.
        return {"id": note_id, **note.dict()}
    else:
        #else, it will raises an exception as note not found.
        raise HTTPException(status_code=404, detail="Note not found.")



#Creating a put method for editing the notes.
@app.put("/notes/{note_id}")
#defining a function with argument note_id as type in and note being a instance of Notes class.
def edit_notes(note_id: int, note: Notes):
    #Here, if note_id is not in notes list, it raises an exception about note not found.
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found.")
    else:
        notes[note_id] = note#here, note is the new note that will replace the old one. 
        return {"id": note_id, **note.dict()}



#Creating a delete method for deleting the note based on the id provided.
@app.delete("/notes/{note_id}")
#defining a delete_note function here with note_id as agrument.
def delete_note(note_id: int):
    #Here, if note_id is not in notes list, it raises an exception about note not found.
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found.")
        #else it will delete the respective note from the note_id.
    else:
        del notes[note_id]#here, notes is the list and inside the big bracet is note_id from which the respective note is identified.
        #returning a message after the note is deleted successfully.
        return {"message": "Note deleted successfully."}
