from fastapi import FastAPI, status, Body, Depends
from auth import get_current_user
from json_func import read_notes_from_file, write_notes_to_file
from pydantic import BaseModel

app = FastAPI()
notes_db = {}


class NoteCreate(BaseModel):
    id: int
    notes: str


@app.post('/note', status_code=status.HTTP_201_CREATED)
async def add_note(current_user: dict = Depends(get_current_user), note: str = Body()) -> str:
    if current_user['username'] not in notes_db:
        notes_db[current_user["username"]] = [note]
    else:
        notes_db[current_user["username"]].append(note)
    write_notes_to_file(notes_db)
    return f'Note created'


@app.get('/notes/user_notes')
async def get_notes(current_user: dict = Depends(get_current_user)):
    notes = read_notes_from_file()
    user_notes = notes.get(current_user['username'])
    return user_notes
