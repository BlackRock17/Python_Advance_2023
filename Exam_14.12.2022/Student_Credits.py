def students_credits(*args):
    collected_credits = 0
    result = {}
    output = []
    for line in args:
        info = line.split("-")
        course = info[0]
        credit = int(info[1])
        test_points = int(info[2])
        hero_points = int(info[3])

        collected_credits += (hero_points / test_points) * credit

        result[course] = (hero_points / test_points) * credit
    sorted_result = dict(sorted(result.items(), key=lambda x: -x[1]))

    if collected_credits >= 240:
        output.append(f"Diyan gets a diploma with {collected_credits:.1f} credits.")
    else:
        output.append(f"Diyan needs {240 - collected_credits:.1f} credits more for a diploma.")

    for key, value in sorted_result.items():
        output.append(f"{key} - {value:.1f}")

    return "\n".join(output)

