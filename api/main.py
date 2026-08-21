from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

class Task(BaseModel):
    message: str

conn = psycopg2.connect(os.environ['DATABASE_URL'])
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, message TEXT)')
conn.commit()

@app.post('/tasks')
def create_task(task: Task):
    cursor.execute('INSERT INTO tasks (message) VALUES (%s) RETURNING id', (task.message,))
    conn.commit()
    return {'id': cursor.fetchone()[0]}