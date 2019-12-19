from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import uvicorn

app = FastAPI()


class Words(BaseModel):
    id: int
    word: str
    translation: str
    done: bool = None


class CreateWord(BaseModel):
    word: str
    translation: str


class EditWord(BaseModel):
    word: str
    translation: str
    done: bool


dictionary = [
    {
        'id': 1,
        'word': 'table',
        'translation': 'стіл',
        'done': False
    },
    {
        'id': 2,
        'word': 'chair',
        'translation': 'крісло',
        'done': False
    }
]

my_words: List[Words] = dictionary


@app.get("/")
def read_root():
    return {"Dictionary"}


@app.get("/words", response_model=List[Words])
def read_task():
    return my_words


@app.get("/word/{word_id}", response_model=Words)
def save_word(word_id: int):
    task = list(filter(lambda t: t['id'] == word_id, my_words))
    return task[0]


@app.post("/create/word", response_model=Words, status_code=201)
def create_word(w: CreateWord):
    task = {
        'id': 44,
        'word': w.word,
        'translation': w.translation,
        'done': False
    }
    dictionary.append(task)
    return task


@app.put("/words/{word_id}", response_model=Words)
def edit_words(word_id, w: EditWord):
    new_word = {
        'id': word_id,
        'word': w.word,
        'translation': w.translation,
        'done': w.done
    }
    return new_word


@app.delete("/words/{word_id}", response_model=List[Words], status_code=201)
def delete_words(word_id: int):
    words = list(filter(lambda t: t['id'] != word_id, my_words))
    return words