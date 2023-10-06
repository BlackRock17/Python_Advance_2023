from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = deque([int(x) for x in input().split()])

result = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while True:
    if len(textiles) == 0 and len(medicaments) == 0:
        print("Textiles and medicaments are both empty.")
        break
    elif len(textiles) == 0:
        print("Textiles are empty.")
        break
    elif len(medicaments) == 0:
        print("Medicaments are empty.")
        break

    textile = textiles.popleft()
    medicament = medicaments.pop()
    sum_ = textile + medicament

    if sum_ == 30:
        result["Patch"] += 1

    elif sum_ == 40:
        result["Bandage"] += 1

    elif sum_ == 100:
        result["MedKit"] += 1

    elif sum_ > 100:
        result["MedKit"] += 1
        try:
            medicament_2 = medicaments.pop()
            medicaments.append(sum_ - 100 + medicament_2)
        except:
            medicaments.append(sum_ - 100)

    else:
        medicaments.append(medicament + 10)

sorted_result = dict(sorted(result.items(), key=lambda x: (-x[1], x[0])))

for key, value in sorted_result.items():
    if value > 0:
        print(f"{key} - {value}")

if medicaments:
    medicaments = [str(x) for x in list(reversed(medicaments))]
    print(f"Medicaments left: {', '.join(medicaments)}")
if textiles:
    textiles = [str(x) for x in textiles]
    print(f"Textiles left: {', '.join(textiles)}")




