## GPA application
print('hello in gpa calculator application .')

while True:
    try:
        n = int(input("Enter the number of subject :"))
        if n <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")
        continue

marks = []
for i in range(n):
    try:
        subject_input = input(f"please enter  mark of subject {i+1} : ")
        subject = int(subject_input)

        if subject < 0 or subject > 100:
            print("Please enter a valid mark between 0 and 100.")
        else:
            marks.append(subject)

    except ValueError:
        print("Please enter a valid number.")


percentage = float(sum(marks)) / (len(marks) * 100)
gpa = round(percentage * 4, 2)

if gpa >= 3.7:
    grade = 'A'

elif gpa >= 3:
    grade = 'B'

elif gpa >= 2.3:
    grade = 'C+'

elif gpa >= 1.7:
    grade = 'C-'

elif gpa >= 1:
    grade = 'D'

else:
    grade = 'F'

print(f"Your GPA is: {gpa} and your grade is: {grade}")
print('Thank you for use our application ...')