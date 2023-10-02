from collections import deque

food = deque(int(x) for x in input().split(", "))
stamina = deque(int(x) for x in input().split(", "))
win = False
days = 0

peaks = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}

while True:
    daily_energy = food.pop() + stamina.popleft()
    days += 1

    for peak, diff in peaks.items():
        if diff == "w":
            continue

        if daily_energy >= diff:
            peaks[peak] = "w"

            if peaks["Kamenitza"] == "w":
                win = True

        break

    if win:
        break

    if not food or not stamina or days == 7:
        break

if win:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks["Vihren"] == "w":
    print("Conquered peaks:")

    for p, d in peaks.items():
        if d == "w":
            print(p)
