# To-do list dictionary
todo_list = {}

def add_task(task):
    task_id = len(todo_list) + 1
    todo_list[task_id] = {'task': task, 'done': False}
    print(f"Task {task_id} added.")

def view_tasks():
    if todo_list:
        for task_id, details in todo_list.items():
            status = "Done" if details['done'] else "Not Done"
            print(f"{task_id}. {details['task']} - {status}")
    else:
        print("No tasks to display.")

def mark_done(task_id):
    if task_id in todo_list:
        todo_list[task_id]['done'] = True
        print(f"Task {task_id} marked as done.")
    else:
        print(f"Task {task_id} not found.")

while True:
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark
