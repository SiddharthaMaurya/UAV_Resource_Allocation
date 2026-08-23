import csv

import random;

class Task:

    def generate_tasks(number):

        tasks = []

        priorities = ["High", "Medium" , "Low"]

        for i in range(number):
            task = Task(
                task_id=i + 1,
                size_mb=random.randint(10, 100),
                cpu_cycles=random.randint(1000, 10000),
                priority=random.choice(priorities),
                deadline=random.randint(1, 10)
            )
            tasks.append(task)
        return tasks

    def __init__(self, task_id, size_mb, cpu_cycles, priority, deadline):

        self.task_id = task_id
        self.size_mb = size_mb
        self.cpu_cycles = cpu_cycles
        self.priority = priority
        self.deadline = deadline


    def display(self):
        print(f"Task ID: {self.task_id}")
        print(f"Size (MB): {self.size_mb}")
        print(f"CPU Cycles: {self.cpu_cycles}")
        print(f"Priority: {self.priority}")
        print(f"Deadline: {self.deadline}")

def save_tasks_to_csv(tasks):

    with open("data/tasks.csv", "w" , newline="") as file:

        writer = csv.writer(file)

        # Header 
        writer.writerow([
            "Task_ID",
            "Size_MB",
            "CPU_Cycles",
            "Priority",
            "Deadline"
        ])

        #Data

        for task in tasks:

            writer.writerow([
                task.task_id,
                task.size_mb,
                task.cpu_cycles,
                task.priority,
                task.deadline
            ])