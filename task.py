tasks = []

while True:
    task = input("Add task (or 'q' to quit): ")
    if task == "q":
        break
    tasks.append(task)

print("Your tasks:", tasks)
