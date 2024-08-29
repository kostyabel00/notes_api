import json


def write_notes_to_file(note):
    with open('data/notes.json', 'w') as f:
        json.dump(note, f)


def read_notes_from_file():
    with open('data/notes.json', 'r') as f:
        return json.load(f)

