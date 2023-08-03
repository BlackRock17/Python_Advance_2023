from collections import deque

queue_ = deque()

while True:
    name = input()

    if name == "End":
        print(f"{len(queue_)} people remaining.")
        break

    if name == "Paid":
        print("\n".join(queue_))
        queue_.clear()

    else:
        queue_.append(name)