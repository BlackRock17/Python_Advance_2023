def gather_credits(credits_needed: int, *args):
    courses = []
    credits = 0

    for course, points in args:
        if credits < credits_needed and course not in courses:
            courses.append(course)
            credits += points

        if credits >= credits_needed:
            break

    if credits >= credits_needed:
        return f"Enrollment finished! Maximum credits: {credits}.\nCourses: {', '.join(sorted(courses))}"
    else:
        return f"You need to enroll in more courses! You have to gather {credits_needed - credits} credits more."

