subjects = {"Math": 90, "Science": 120}

total_study_time = 0

for subject, minutes in subjects.items():
    print(f"{subject}: {minutes} minutes")
    total_study_time += minutes

breaks = (total_study_time - 1) // 45
total_time = total_study_time + breaks * 15

print(f"Total time: {total_study_time} minutes")
print(f"Total time including breaks: {total_time} minutes")
