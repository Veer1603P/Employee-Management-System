#Assignment 2: Employee Directory and Management System
import os
EMP_FOLDER = "Employee"
if not os.path.exists(EMP_FOLDER):
    os.makedirs(EMP_FOLDER)
    
def get_Filename(data):
    name = data.get("name")
    company = data.get("company_name")
    if company:
        return f"{name}_{company}.txt"
    else:
        return f"{name}.txt"

def add_employee():
    while True:
        print("\n--- ADD NEW EMPLOYEE DETAILS ---")

        name = input("Enter the name of the employee (mandatory): ")
        if not name:
            print("Name is required.")
            continue  

        email = input("Enter the employee email (must contain '@'): ")
        if '@' not in email:
            print("Invalid email. It must contain '@'.")
            continue

        location = input("Enter the location of the employee (mandatory): ")
        if not location:
            print("Location is required.")
            continue

        age_input = input("Enter the age of the employee (18 to 60): ")
        if age_input.isdigit():
            age = int(age_input)
            if age < 18 or age > 60:
                print("Age must be between 18 and 60.")
                continue
        else:
            print("Age must be a number.")
            continue

        company_name = input("Enter the company name (optional): ")
        company_loc = input("Enter the company location (optional): ")

        employee_data = {
            "name": name,
            "email": email,
            "location": location,
            "age": age,
        }

        if company_name:
            employee_data["company_name"] = company_name
        if company_loc:
            employee_data["company_loc"] = company_loc

        file_name = get_Filename(employee_data)
        file_path = EMP_FOLDER + "/" + file_name

        with open(file_path, 'w') as file:
            for key, value in employee_data.items():
                file.write(f"{key}: {value}\n")

        print(f" Employee data saved to: {file_path}")
        break 

def show_details():
    while True:
        print("\n--- SHOW EMPLOYEE DETAILS---")
        file_name = input("Enter employee file name (with .txt): ")
        file_path = EMP_FOLDER + "/" + file_name 

        if not os.path.exists(file_path):
            print("File not found. Try again.")
            continue

        with open(file_path, 'r') as file:
            print("\nEmployee Details:")
            for content in file:
                print(content)
        break

def edit_details():
    while True:
        print("\n--- EDIT EMPLOYEE DETAILS ---")
        file_name = input("Enter employee file name (with .txt): ")
        file_path = EMP_FOLDER + "/" + file_name  

        if not os.path.exists(file_path):
            print("File not found. Try again.")
            continue

        with open(file_path, 'r') as file:
            data = {}
            for line in file:
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    data[key] = value

        print("\nCurrent Data:")
        for k, v in data.items():
            print(f"{k}: {v}")

        while True:
            print("\nData Manipulation Options:")
            print("1. Edit a field")
            print("2. Delete a field")
            print("3. Add new key-value pair")
            print("4. Go Back")
            choice = input("Enter your choice: ")

            if choice == "1":
                key = input("Enter key(name , email , location , age , company_name , company_loc) to edit: ")
                if key in data:
                    new_value = input(f"Enter new value for {key}: ")
                    data[key] = new_value
                    print("Key edited successfully")
                else:
                    print("Key not found.")
            elif choice == "2":
                key = input("Enter key(name , email , location , age , company_name , company_loc) to delete: ")
                if key in data:
                    del data[key]
                    print("Key deleted successfully ")
                else:
                    print("Key not found.")
            elif choice == "3":
                key = input("Enter new key: ")
                value = input("Enter value: ")
                data[key] = value
            elif choice == "4":
                break
            else:
                print("Invalid choice.")

        with open(file_path, 'w') as file:
            for k, v in data.items():
                file.write(f"{k}: {v}\n")

        print("Details updated successfully.")
        break

def resign_employee():
    while True:
        print("\n--- EMPLOYEE RESIGNATION ---")
        file_name = input("Enter employee file name (with .txt): ")
        file_path = EMP_FOLDER + "/" + file_name  

        if not os.path.exists(file_path):
            print("File not found. Try again.")
            continue

        with open(file_path, 'r') as file:
            data = {}
            for line in file:
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    data[key] = value

        if "company_name" not in data:
            print("This employee is not associated with any company.")
            break

        reason = input("Enter reason for resignation: ")
        data["reason"] = reason
        del data["company_name"]
        data.pop("company_loc", None)

        with open(file_path, 'w') as file:
            for k, v in data.items():
                file.write(f"{k}: {v}\n")

        print("Resignation processed successfully.")
        break

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM=====")
    print("1. ADD NEW EMPLOYEE")
    print("2. SHOW DETAILS")
    print("3. EDIT EXISTING DETAILS")
    print("4. RESIGN")
    print("5. EXIT")

    option = input("Choose an option: ")

    if option == "1":
        add_employee()
    elif option == "2":
        show_details()
    elif option == "3":
        edit_details()
    elif option == "4":
        resign_employee()
    elif option == "5":
        print("Exiting the management system. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

