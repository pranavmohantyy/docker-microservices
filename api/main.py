from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class Task(BaseModel):
    message: str

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, message TEXT)')
conn.commit()

@app.post('/tasks')
def create_task(task: Task):
    cursor.execute('INSERT INTO tasks (message) VALUES (?)', (task.message,))
    conn.commit()
    return {'id': cursor.lastrowid}
