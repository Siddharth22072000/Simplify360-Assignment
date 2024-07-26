"""
Question 1:

We have a large and complex workflow, made of tasks. And
have to decide who does what, when, so it all gets done on time.
All tasks have dependency on other tasks to complete
Each task(t) has a
D[t] = duration of task
EFT[t] = the earliest finish time for a task
LFT[t] = the latest finish time for a task
EST[t] = the earliest start time for a task
LST[t] = the last start time for a task
Assume
that “clock” starts at 0 (project starting time).
We are given the starting task T_START where the EST[t] = 0 and LST[t] = 0
You have to write an Java/Python/JS/Typescript console application to answer the following questions
Earliest time all the tasks will be completed?
Latest time all tasks will be completed?

"""

# Importing the required libraries
from collections import defaultdict, deque

# Task class to hold task details
class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.dependencies = []
        self.dependents = []
        self.est = 0
        self.eft = 0
        self.lft = float('inf')
        self.lst = float('inf')

def parse_input(tasks_data):
    tasks = {}
    for task_name, duration in tasks_data.items():
        tasks[task_name] = Task(task_name, duration)
    return tasks

def calculate_earliest_times(tasks):
    queue = deque([task for task in tasks.values() if not task.dependencies])
    while queue:
        task = queue.popleft()
        task.eft = task.est + task.duration
        for dependent in task.dependents:
            dependent.est = max(dependent.est, task.eft)
            queue.append(dependent)

def calculate_latest_times(tasks, max_eft):
    for task in tasks.values():
        if not task.dependents:
            task.lft = max_eft
            task.lst = task.lft - task.duration
    queue = deque([task for task in tasks.values() if not task.dependents])
    while queue:
        task = queue.popleft()
        for dependency in task.dependencies:
            dependency.lft = min(dependency.lft, task.lst)
            dependency.lst = dependency.lft - dependency.duration
            queue.append(dependency)

def main():
    tasks_data = {
        'T1': 5,
        'T2': 3,
        'T3': 2,
        'T4': 4
    }
    
    dependencies = {
        'T2': ['T1'],
        'T3': ['T1'],
        'T4': ['T2', 'T3']
    }
    
    tasks = parse_input(tasks_data)
    for task_name, deps in dependencies.items():
        for dep in deps:
            tasks[task_name].dependencies.append(tasks[dep])
            tasks[dep].dependents.append(tasks[task_name])
    
    calculate_earliest_times(tasks)
    max_eft = max(task.eft for task in tasks.values())
    calculate_latest_times(tasks, max_eft)
    
    print("Earliest time all tasks will be completed:", max_eft)
    latest_completion_time = max(task.lft for task in tasks.values())
    print("Latest time all tasks will be completed:", latest_completion_time)

if __name__ == "__main__":
    main()



"""
Time Complexity:

1. Parsing the Input: Assuming that parsing the input involves reading task information
and dependencies once, it would take O(V + E) time, where V is the number of tasks and
E is the number of dependencies.

2. Calculating Earliest Finish Time (EFT): Each task is visited once, and each dependency
is checked once. Therefore, this step takes O(V + E) time.

3. Calculating Latest Finish Time (LFT): Similar to EFT calculation, each task and each
dependency is visited once. Thus, this step also takes O(V + E) time.

Overall, the time complexity is O(V + E) due to the linear traversal of tasks and dependencies.

Space Complexity:

1. Storing Tasks and Dependencies: The tasks are stored in a dictionary or similar structure,
requiring O(V) space. The dependencies (both forward and backward) are stored in adjacency
lists, requiring O(E) space.

2. Queue for Traversals: The maximum size of the queue in the worst case is O(V).

Overall, the space complexity is O(V + E) for storing tasks and dependencies.

Summary:

Time Complexity: O(V + E)
Space Complexity: O(V + E)

"""
