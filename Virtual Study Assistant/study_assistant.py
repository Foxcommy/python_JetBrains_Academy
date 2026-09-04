subjects = {}

while True:
    subject = input("Enter subject name: ")

    if subject == "":
        break

    while True:
        try:
            time = int(input(f"Enter time allocated for {subject}: "))
            if time > 0:  # Проверяем, что время положительное
                break
            else:
                print("Invalid input! Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    subjects[subject] = time

# Выводим словарь только если он не пустой
if subjects:
    print(f'subjects = {subjects}')
