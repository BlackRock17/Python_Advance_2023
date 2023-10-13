from collections import deque

eggs = deque(map(int, input().split(", ")))
paper = deque(map(int, input().split(", ")))
boxes = 0

while eggs and paper:
    egg = eggs.popleft()

    if egg <= 0:
        continue

    piece_paper = paper.pop()

    if egg == 13:
        second_paper = paper.popleft()
        paper.appendleft(piece_paper)
        paper.append(second_paper)
        continue

    if egg + piece_paper <= 50:
        boxes += 1

if boxes:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(list(map(str, eggs)))}")
if paper:
    print(f"Pieces of paper left: {', '.join(list(map(str, paper)))}")