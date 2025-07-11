# NoteAPI
A NoteAPI is just a RESTful API (or web API) that lets users create, read, update, and delete (CRUD) notes through HTTP requests.

# Features

- Create new notes (title and content required)  
- Retrieve all notes  
- Retrieve a single note by ID  
- Update an existing note by ID  
- Delete a note by ID  
- Input validation with Pydantic models  
- Auto-generated interactive API docs with Swagger UI  

## Requirements

- Python 3.7+  
- FastAPI  
- Uvicorn (ASGI server) 

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/noteapi.git
   cd noteapi

2. (Optional) Create and activate a virtual environment:

- On Linux/macOS:
  ```bash
  python -m venv venv
  source venv/bin/activate
  venv\Scripts\activate  //windows

3. Install dependencies:
   ```bash
    pip install fastapi uvicorn
    #or directly download the requirement file
    pip install -e requirements.txt

4. Running the API
   Start the server with:
   ```bash
   uvicorn file_name:app --reload

- The API will be available at: http://127.0.0.1:8000
- Interactive docs at: http://127.0.0.1:8000/docs


## API Endpoints

| Method | Endpoint      | Description             | Request Body                    | Response                      |
| ------ | ------------- | ----------------------- | -------------------------------- | ----------------------------- |
| POST   | `/notes/`     | Create a new note       | JSON with `title` and `content` | Created note with ID and data |
| GET    | `/notes/`     | Get all notes           | None                             | List of all notes             |
| GET    | `/notes/{id}` | Get a note by its ID    | None                             | Note data with ID             |
| PUT    | `/notes/{id}` | Update a note by its ID | JSON with `title` and `content` | Updated note data with ID     |
| DELETE | `/notes/{id}` | Delete a note by its ID | None                             | Success message               |
