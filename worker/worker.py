import psycopg2
import time
import os

def process_tasks():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cursor = conn.cursor()
    while True:
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        for task in tasks:
            print(f'Processing task {task[0]}: {task[1]}')
            time.sleep(2)
        time.sleep(5)

if __name__ == '__main__':
    process_tasks()