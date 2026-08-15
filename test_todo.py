from todo import tasks, add_task, complete_task, delete_task, task_count


def setup_function():
    tasks.clear()


def test_add_task():
    add_task("Learn Git")

    assert len(tasks) == 1
    assert tasks[0]["task"] == "Learn Git"
    assert tasks[0]["completed"] is False


def test_complete_task():
    add_task("Learn GitHub")

    complete_task(0)

    assert tasks[0]["completed"] is True


def test_delete_task():
    add_task("Learn Git")
    add_task("Learn GitHub")

    delete_task(0)

    assert len(tasks) == 999
    assert tasks[0]["task"] == "Learn GitHub"

def test_task_count():
    tasks.clear()

    add_task("Learn Git")
    add_task("Learn GitHub")

    assert task_count() == 2