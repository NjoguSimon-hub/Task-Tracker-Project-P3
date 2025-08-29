📋 Task Tracker CLI
📌 Description
Task Tracker CLI is a Python Command Line Interface (CLI) application that helps users manage tasks.
It uses SQLAlchemy ORM with a SQLite database.

Features include:

Create and list users

Assign tasks to users

View all tasks or tasks by user

Update tasks (mark complete/incomplete)

Delete tasks

🛠️ Installation
Clone this repository:

git clone <your-repo-url>
cd task_tracker
Install dependencies with Pipenv:

pipenv install
pipenv shell
pipenv install sqlalchemy alembic ipdb
🗄️ Database Setup
Run this command once to create the database:

python -c "from lib.models import init_db; init_db()"
This will create a file called tasks.db.

▶️ Usage
Run the CLI:

python lib/cli.py
You’ll see the menu:

📋 Task Tracker CLI
1. Create User
2. List Users
3. Add Task
4. List All Tasks
5. List Tasks by User
6. Update Task (toggle complete)
7. Delete Task
0. Exit
📂 File Guide
lib/cli.py → Main CLI menu & loop

lib/helpers.py → Functions for user & task management

lib/models.py → SQLAlchemy models & database setup

README.md → Project documentation

📊 Models
User
id → primary key

name → user’s name

email → unique email

tasks → relationship: one user has many tasks

Task
id → primary key

title → task title

description → task details

completed → boolean (default = False)

user_id → foreign key linking task to user

✅ Example Run
📋 Task Tracker CLI
1. Create User
2. List Users
3. Add Task
4. List All Tasks
5. List Tasks by User
6. Update Task (toggle complete)
7. Delete Task
0. Exit
> 1
Enter user name: Alice
Enter email: alice@email.com
✅ User Alice added!

> 3
Enter user ID to assign task: 1
Enter task title: Study Python
Enter description: ORM relationships
✅ Task 'Study Python' added for Alice!

> 4
1. Study Python (Alice) - ❌
📚 Resources
SQLAlchemy Documentation

Alembic Documentation"
