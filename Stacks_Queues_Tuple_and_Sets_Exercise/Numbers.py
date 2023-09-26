def add_num(num, set_numbers):
    for index in range(2, len(num)):
        set_numbers.add(int(num[index]))
    return set_numbers


def remove_num(num, set_numbers):
    for index in range(2, len(num)):
        if int(num[index]) in set_numbers:
            set_numbers.remove(int(num[index]))
    return set_numbers


first_line = set(int(x) for x in input().split())
second_line = set(int(x) for x in input().split())

N = int(input())

for i in range(N):
    command = input()

    if "Add First" in command:
        action = command.split()
        add_num(action, first_line)

    elif "Add Second" in command:
        action = command.split()
        add_num(action, second_line)

    elif "Remove First" in command:
        action = command.split()
        remove_num(action, first_line)

    elif "Remove Second" in command:
        action = command.split()
        remove_num(action, second_line)

    elif "Check Subset" in command:
        if first_line.issubset(second_line) or second_line.issubset(first_line):
            print("True")
        else:
            print("False")

first_line = list(sorted(first_line))
second_line = list(sorted(second_line))

print(*first_line, sep=", ")
print(*second_line, sep=", ")


#### SECOND_SOLUTION

first_seq = set([int(x) for x in input().split()])
second_seq = set([int(x) for x in input().split()])

N = int(input())

for _ in range(N):
    command_args = input()

    if "Add First" in command_args:
        command = command_args.split()
        for el in command:
            if el.isdigit():
                first_seq.add(int(el))

    elif "Add Second" in command_args:
        command = command_args.split()
        for el in command:
            if el.isdigit():
                second_seq.add(int(el))

    elif "Remove First" in command_args:
        command = command_args.split()
        for el in command:
            if el.isdigit() and int(el) in first_seq:
                first_seq.remove(int(el))

    elif "Remove Second" in command_args:
        command = command_args.split()
        for el in command:
            if el.isdigit() and int(el) in second_seq:
                second_seq.remove(int(el))

    else:
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print('True')
        else:
            print('False')

first_seq = list(sorted(first_seq))
second_seq = list(sorted(second_seq))

print(*first_seq, sep=", ")
print(*second_seq, sep=", ")
