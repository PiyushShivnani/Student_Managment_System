class Student:
    def __init__(self, name, roll_number, marks1,marks2):
        self.name = name
        self.roll_number = roll_number
        self.marks1 = marks1
        self.marks2 = marks2
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        num=int(input("How many students data you want to enter: "))
        for i in range(num):
            print("Enter data of student",i+1)
            while True:
                name = input("Enter student name: ")
                roll_number = input("Enter student roll number: ")
                if self.is_roll_number_duplicate(roll_number):
                    print(f"Student with roll_number '{roll_number}' already exists. Please enter data of student again!!")
                else:
                    break    
            marks1 = input("Enter student Marks1: ")
            marks2 = input("Enter student Marks2: ")
            student = Student(name, roll_number, marks1, marks2)
            self.students.append(student)
            print(f"Student '{name}' added successfully!\n")
    
    def is_roll_number_duplicate(self,roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return True
        return False    

    def search_student(self):
        roll_number = input("Enter student roll number: ")
        for student in self.students:
            if student.roll_number == roll_number:
                print("Student found:")
                print(f"Name: {student.name}")
                print(f"Roll Number: {student.roll_number}")
                print(f"Marks1: {student.marks1}")
                print(f"Marks2: {student.marks2}")
                return
        print(f"Student with roll number '{roll_number}' not found.")

    def remove_student(self):
        option=input("Do you want to delete all student records?(yes/no): ")
        if option.lower() == "yes" or option.lower() == "y":
            self.students = []
            print("All student records have been deleted")
            return
        elif option.lower() == "no" or option.lower() == "n":
            roll_number = input("Enter student roll number: ")
            for student in self.students:
                if student.roll_number == roll_number:
                    self.students.remove(student)
                    print(f"Student with roll number '{roll_number}' removed successfully!")
                    return
            print(f"Student with roll number '{roll_number}' not found.")
        else:
            print("Invalid choice. Please try again!!")

    def update_student(self):
        roll_number = input("Enter student roll number: ")
        for student in self.students:
            if student.roll_number == roll_number:
                print(f"Previous details of student with roll number '{roll_number}' is:")
                print(f"Name: {student.name}")
                print(f"Marks1: {student.marks1}")
                print(f"Marks2: {student.marks2}")
                print("\nEnter new student details:")
                name = input("Name: ")
                marks1 = input("Marks1: ")
                marks2 = input("Marks2: ")
                student.name = name
                student.marks1 = marks1
                student.marks2 = marks2
                print(f"Student with roll number '{roll_number}' updated successfully!")
                return
        print(f"Student with roll number '{roll_number}' not found.")

    def display_students(self):
        if not self.students:
            print("No students found.")
            return

        print("Student List:")
        print("--------------")
        for student in self.students:
            print(f"Name: {student.name}")
            print(f"Roll Number: {student.roll_number}")
            print(f"Marks1: {student.marks1}")
            print(f"Marks2: {student.marks2}")
            print("--------------")


obj = StudentManagementSystem()

while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("------------------------")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Remove Student")
    print("4. Update Student")
    print("5. Display Students")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        obj.add_student()
    elif choice == "2":
        obj.search_student()
    elif choice == "3":
        obj.remove_student()
    elif choice == "4":
        obj.update_student()
    elif choice == "5":
        obj.display_students()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")