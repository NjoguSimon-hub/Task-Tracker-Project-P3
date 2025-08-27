from models import Session, User, Task

session = Session()

def create_user():
    name = input("Enter user name: ")
    email = input("Enter email: ")
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    print(f"✅ User {name} added!")

def list_users():
    users = session.query(User).all()
    if users:
        for user in users:
            print(user)
    else:
        print("No users found!")

def add_task():
    list_users()
    user_id = input("Enter user ID to assign task: ")
    user = session.query(User).get(user_id)
    if not user:
        print("❌ User not found.")
        return
    title = input("Enter task title: ")
    description = input("Enter description: ")
    task = Task(title=title, description=description, user=user)
    session.add(task)
    session.commit()
    print(f"✅ Task '{title}' added for {user.name}!")

def list_tasks():
    tasks = session.query(Task).all()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks found!")

def list_tasks_by_user():
    list_users()
    user_id = input("Enter user ID: ")
    user = session.query(User).get(user_id)
    if not user:
        print("❌ User not found.")
        return
    tasks = session.query(Task).filter(Task.user_id == user.id).all()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print(f"No tasks found for {user.name}!")

def update_task():
    list_tasks()
    task_id = input("Enter task ID to toggle: ")
    task = session.query(Task).get(task_id)
    if task:
        task.completed = not task.completed
        session.commit()
        status = "completed" if task.completed else "incomplete"
        print(f"✅ Task marked as {status}!")
    else:
        print("❌ Task not found")

def delete_task():
    list_tasks()
    task_id = input("Enter task ID to delete: ")
    task = session.query(Task).get(task_id)
    if task:
        session.delete(task)
        session.commit()
        print("✅ Task deleted!")
    else:
        print("❌ Task not found")

def exit_program():
    print("Goodbye 👋")
    exit()