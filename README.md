# To-Do App

This is a simple command-line to-do app built with Python and SQLite3. 

Toy app, easy modify. Even db is just created on home directory directly. Cus I just want db file easily using like `scp` or `rsync` to transfer between different pc.

but it's work!

## Features

- Add tasks with status(TODO, HOLD, DONE, CANCELED) and content
- List tasks in table format
- Store data in a SQLite3 database

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

Clone the repository or download the script:
```bash
git clone https://github.com/yourusername/todo-app.git
```

## Build
require `pyinstaller`
```bash
pip install pyinstaller
```

```bash
make 
mv dist/todo /usr/local/bin/
```

## Usage
1. Add todo task
```bash
todo add "Your task" 
```
or with content/remark
```bash
todo add "Your task description" --content "Your task content"

```

2. list task
```bash
todo list
```

3. delete task
```bash
todo delete TASK_ID
```

4. update task status or content
```bash
todo update TASK_ID --status STATUS --content "New content.." 
```
