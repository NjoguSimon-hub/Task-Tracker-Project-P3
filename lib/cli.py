from helper import (
    create_user, list_users, add_task, list_tasks, 
    list_tasks_by_user, update_task, delete_task, exit_program
)

def menu():
    print("\n📋 Task Tracker CLI")
    print("1. Create User")
    print("2. List Users")
    print("3. Add Task")
    print("4. List All Tasks")
    print("5. List Tasks by User")
    print("6. Update Task (toggle complete)")
    print("7. Delete Task")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            create_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            add_task()
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            list_tasks_by_user()
        elif choice == "6":
            update_task()
        elif choice == "7":
            delete_task()
        elif choice == "0":
            exit_program()
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main() 