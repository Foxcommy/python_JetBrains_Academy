# Write your solution here
subject = input()
total_study_time = 0
total_time = 0

for key, value in subjects.items():
    print(f"{key}: {value} minutes")
    total_study_time += value

total_time = (total_study_time//45)*15 + total_study_time

print(f"Total time: {total_study_time} minutes")
print(f"Total time including breaks: {total_time} minutes")
