import os
import time
import redis
import psycopg2


def process_tasks():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cursor = conn.cursor()
    r = redis.Redis.from_url(os.environ['REDIS_URL'])
    while True:
        task = r.blpop('task_queue')
        if task:
            task_id, task_message = task[1].decode('utf-8').split(':', 1)
            print(f'Processing task {task_id}: {task_message}')
            time.sleep(2)
        time.sleep(5)


if __name__ == '__main__':
    process_tasks()