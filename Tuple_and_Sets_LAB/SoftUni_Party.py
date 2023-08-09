N = int(input())

guests = set()

for i in range(N):
    code = input()
    if len(code) != 8:
        continue
    else:
        guests.add(code)

arrived_guests = set()

while True:
    arrive_guest = input()

    if arrive_guest == "END":
        break
    else:
        arrived_guests.add(arrive_guest)

result = sorted(guests.difference(arrived_guests))

print(len(result))
for ticket in result:
    print(ticket)


