tasks = ["Buy groceries"]


def add_task(task):
    tasks.append({"task": task, "completed": False})


def view_tasks():
    return tasks


def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True


def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def task_count():
    return len(tasks)


if __name__ == "__main__":
    add_task("Learn Git")
    add_task("Learn GitHub")

    print("Tasks:")
    print(view_tasks())

    complete_task(0)

    print("\nAfter completing first task:")
    print(view_tasks())

    delete_task(1)

    print("\nAfter deleting second task:")
    print(view_tasks())