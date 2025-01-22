import pandas as pd
import os

EXCEL_FILE = r"C:\Users\manee\OneDrive\Desktop\Internship\tasks.csv"

def load_tasks():
    if os.path.exists(EXCEL_FILE):
        try:
            return pd.read_csv(EXCEL_FILE, encoding='utf-8').to_dict('records')
        except UnicodeDecodeError:
            return pd.read_csv(EXCEL_FILE, encoding='latin1').to_dict('records')
        except pd.errors.ParserError:
            print("Error parsing tasks.csv. Ensure the file has a consistent format.")
            return []
    else:
        return []

def save_tasks(tasks):
    df = pd.DataFrame(tasks)
    df.to_csv(EXCEL_FILE, index=False)

def add_task(description, priority):
    priority_mapping = {"High": 1, "Medium": 2, "Low": 3}
    if priority not in priority_mapping:
        print("Invalid priority. Please choose from High, Medium, or Low.")
        return
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "priority": priority
    }
    tasks.append(new_task)
    save_tasks(tasks)

def remove_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != int(task_id)]
    for idx, task in enumerate(tasks):
        task["id"] = idx + 1
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    if tasks:
        priority_mapping = {"High": 1, "Medium": 2, "Low": 3}
        tasks = sorted(tasks, key=lambda x: priority_mapping[x["priority"]])
        print("\nTasks:")
        for task in tasks:
            print(f'{task["id"]}. {task["description"]} (Priority: {task["priority"]})')
    else:
        print("\nNo tasks available.")

def recommend_task():
    tasks = load_tasks()
    if tasks:
        priority_mapping = {"High": 1, "Medium": 2, "Low": 3}
        tasks = sorted(tasks, key=lambda x: priority_mapping[x["priority"]])
        print(f'\nRecommended Task: {tasks[0]["description"]} (Priority: {tasks[0]["priority"]})')
    else:
        print("\nNo tasks available for recommendation.")

def main():
    while True:
        print("\nTask Management App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Recommend Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (High, Medium, Low): ")
            add_task(description, priority)
        elif choice == "2":
            task_id = input("Enter task ID to remove: ")
            remove_task(task_id)
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            recommend_task()
        elif choice == "5":
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
