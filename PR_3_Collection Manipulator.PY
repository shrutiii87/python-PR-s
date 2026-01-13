students = []  

print("Welcome to the Student Data Organizer!")

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    a = input("Enter your choice: ")

    # 1. Add Student
    if a == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        date_of_birth = input("Enter date of birth (dd-mm-yyyy): ")
        subjects = set(input("Enter subjects (comma separated): ").split(","))
      

        student = {
            
            "Date of birth": (student_id, date_of_birth), 
            "student_id" : student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
            
        }

        students.append(student)
        print("Student added successfully!")

    # 2. Display All Students
    elif a == "2":
        if not students:
            print("No student records available.")
        else:
            print("\nAll Students:")
            for i in students:
                print(f"ID: {i['student_id']}| Name: {i['name']}| Age: {i['age']}| "
                      f"Grade: {i['grade']}| Subjects: {', '.join(i['subjects'])}")
  
    # 3. Update Student Information
    elif a == "3":
        stu_id = input("Enter Student ID to update: ")
        found = False
        for i in students:
            if i["Date of birth"][0] == stu_id:
                found = True
                print("What do you want to update?")
                print("1. Age")
                print("2. Subjects")
                opt = input("Enter choice: ")
                if opt == "1":
                    i['age'] = int(input("Enter new age: "))
                    print("Age updated successfully!")
                elif opt == "2":
                    i['subjects'] = set(input("Enter new subjects (comma separated): ").split(","))
                    print("Subjects updated successfully!")
                else:
                    print("Invalid update option.")
                break
        if not found:
            print("Student not found.")

    # 4. Delete Student
    elif a == "4":
        stu_id = input("Enter Student ID to delete: ")
        found = False
        for i in range(len(students)):
            if students[i]['Date of birth'][0] == stu_id:
                del students[i]   
                found = True
                print("Student deleted successfully!")
                break
        if not found:
            print("Student not found.")

    # 5. Display Subjects Offered
    elif a == "5":
        all_subjects = set()
        for i in students:
            all_subjects.update(i['subjects'])
        print("Subjects offered:", ", ".join(all_subjects) if all_subjects else "None")

    # 6. Exit
    elif a == "6":
        print("Thank you for using the Student Data Organizer!")
        break

    else:
        print("Invalid choice. Please try again.")
