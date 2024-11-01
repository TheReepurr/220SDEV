def student_qualification():
    while True:
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name == 'ZZZ':
            print("Exiting program.")
            break
        
        first_name = input("Enter the student's first name: ")
        
        try:
            gpa = float(input("Enter the student's GPA: "))
        except ValueError:
            print("Invalid input. Please enter a numeric GPA.")
            continue

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or Honor Roll.")

# Run the program
student_qualification()
