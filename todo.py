import sqlite3
import argparse
from prettytable import PrettyTable
from datetime import datetime
from termcolor import colored
import os

# Database path
db_path = os.path.expanduser('~/todo.db')

# Database setup
def setup_db():
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT NOT NULL,
            status TEXT NOT NULL,
            content TEXT,
            create_date TEXT NOT NULL,
            last_updated_date TEXT NOT NULL
        )
        ''')
        conn.commit()
        conn.close()
        print("Database created successfully!")

# Add task
def add_task(task, status='TODO', content=''):
    create_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, status, content, create_date, last_updated_date) VALUES (?, ?, ?, ?, ?)', (task, status, content, create_date, create_date))
    conn.commit()
    conn.close()
    print("Task added successfully!")

# List tasks
def list_tasks():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    if tasks:
        table = PrettyTable()
        table.field_names = ["ID", "Task", "Status", "Content", "Create Date", "Last Updated Date"]
        for task in tasks:
            status = task[2]
            if status == 'TODO':
                status_colored = colored(status, 'blue')
            elif status == 'HOLD':
                status_colored = colored(status, 'yellow')
            elif status == 'DONE':
                status_colored = colored(status, 'green')
            elif status == 'CANCELED':
                status_colored = colored(status, 'red')
            else:
                status_colored = status
            table.add_row([task[0], task[1], status_colored, task[3], task[4], task[5]])
        print(table)
    else:
        print("No tasks found.")

# Update task
def update_task(task_id, status=None, content=None):
    last_updated_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    if status:
        cursor.execute('UPDATE tasks SET status = ?, last_updated_date = ? WHERE id = ?', (status, last_updated_date, task_id))
    if content:
        cursor.execute('UPDATE tasks SET content = ?, last_updated_date = ? WHERE id = ?', (content, last_updated_date, task_id))
    conn.commit()
    conn.close()
    print("Task updated successfully!")

# Delete task
def delete_task(task_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("Task deleted successfully!")

# Main function
def main():
    parser = argparse.ArgumentParser(description='Simple To-Do App')
    parser.add_argument('action', choices=['add', 'list', 'delete', 'update'], help='Action to perform')
    parser.add_argument('task_or_id', nargs='?', help='Task description (for add action) or Task ID (for delete/update action)')
    parser.add_argument('--status', choices=['TODO', 'HOLD', 'DONE', 'CANCELED'], help='Task status (for update action)')
    parser.add_argument('--content', help='Task content (for add/update content action)')

    args = parser.parse_args()

    if args.action == 'add':
        if args.task_or_id:
            add_task(args.task_or_id, content=args.content or '')
        else:
            print("Task description is required for add action.")
    elif args.action == 'list':
        list_tasks()
    elif args.action == 'delete':
        if args.task_or_id:
            delete_task(int(args.task_or_id))
        else:
            print("Task ID is required for delete action.")
    elif args.action == 'update':
        if args.task_or_id:
            update_task(int(args.task_or_id), status=args.status, content=args.content)
        else:
            print("Task ID is required for update action.")

if __name__ == '__main__':
    setup_db()
    main()

