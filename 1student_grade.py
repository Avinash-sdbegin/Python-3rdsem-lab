# Task 1: students.txt handling

def create_and_read_students_file():
    filename = "students.txt"
    try:
        # Write student names and grades to file
        with open(filename, "w") as file:
            file.write("Name, Grade\n")
            file.write("AVINASH, 120\n")
            file.write("Ramesh, 92\n")
            file.write("Vivek, 78\n")
            file.write("Shubham, 88\n")
        print(" File written successfully!\n")

        # Read and display the contents
        with open(filename, "r") as file:
            content = file.read()
            print("Contents of students.txt:\n")
            print(content)

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You don’t have permission to access this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

create_and_read_students_file()
