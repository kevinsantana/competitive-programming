"""
You are asked to design a small system to manage a list of pending tasks. You need to implement the following operations:
* 		Add a task: Each task should have a name (string) and a priority (integer from 1 to 5, where 1 is the highest priority). If no priority is specified, it should default to 3.
* 		List tasks: It should display all tasks, ordered by priority (from highest to lowest).
* 		Mark a task as completed: Once completed, the task should be removed from the list.
"""
class Tasks:
    def __init__(self, tasks: list = None) -> None:
        if tasks is None:
            tasks = []
        
        self.tasks = tasks

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks.sort(key=lambda x: x.priority)
    
    def mark_completed(self, task):
        self.tasks.remove(task)

class Task:
    def __init__(self, name: str, priority: int = 3):
        self.name = name
        self.priority = priority
        self.tasks = []

    def __iter__(self):
        for task in self.tasks:
            yield task

    def __repr__(self) -> str:
        return self.name


if __name__ == "__main__":
    tasks = Tasks()

    task1 = Task(name="task1", priority=1)
    tasks.add_task(task1)

    task2 = Task(name="task2")
    tasks.add_task(task2)

    tasks.list_tasks()
    print(tasks.tasks)

    tasks.mark_completed(task1)
    
    tasks.list_tasks()
    print(tasks.tasks)

