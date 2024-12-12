# student details
student_name = input("Enter student name: ")
student_number = input("Enter student number: ")
programming_mark = float(input("Enter programming mark: "))
data_science_mark = float(input("Enter data science mark: "))
computer_applications_mark = float(input("Enter computer applications mark: "))
# average mark
average_mark = (programming_mark + data_science_mark + computer_applications_mark) / 3
# details of the student
print(f"Name: {student_name}")
print(f"Student Number: {student_number}")
print(f"Programming Mark: {programming_mark}")
print(f"Data Science Mark: {data_science_mark}")
print(f"Computer Applications Mark: {computer_applications_mark}")
print(f"Average Mark: {average_mark:.3f}")

