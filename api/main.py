from fastapi import FastAPI
from pydantic import BaseModel
import os
import redis
import psycopg2

app = FastAPI()

class Task(BaseModel):
    message: str

conn = psycopg2.connect(os.environ['DATABASE_URL'])
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, message TEXT)')
conn.commit()

r = redis.Redis.from_url(os.environ['REDIS_URL'])

@app.post('/tasks')
def create_task(task: Task):
    cursor.execute('INSERT INTO tasks (message) VALUES (%s) RETURNING id', (task.message,))
    conn.commit()
    task_id = cursor.fetchone()[0]
    r.rpush('task_queue', f'{task_id}:{task.message}')
    return {'id': task_id}