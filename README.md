-----

# Employee Directory and Management System

This Python script provides a simple command-line interface for managing employee records. It allows you to add new employees, view their details, edit existing information, and process employee resignations. Employee data is stored in individual text files within an "Employee" directory.

-----

## Features

  * **Add New Employee**: Create a new employee record with details such as name, email, location, age, and optional company information.
  * **Show Employee Details**: Retrieve and display the complete details of a specific employee by entering their file name.
  * **Edit Existing Details**: Modify an employee's record by editing, deleting, or adding new key-value pairs to their data.
  * **Process Resignation**: Mark an employee as resigned, which removes their company details and adds a reason for resignation.
  * **Data Persistence**: Employee data is saved in plain text files, ensuring information is retained between sessions.

-----

## Getting Started

These instructions will help you set up and run the Employee Directory and Management System on your local machine.

### Prerequisites

You need Python 3.x installed on your system.

### Installation

1.  **Save the Script**: Save the provided Python code into a file named, for example, `employee_manager.py`.

2.  **Run the Script**: Open a terminal or command prompt, navigate to the directory where you saved the file, and run the script using the Python interpreter:

    ```bash
    python employee_manager.py
    ```

-----

## How to Use

Once the script is running, you'll see a menu with several options:

```
===== EMPLOYEE MANAGEMENT SYSTEM=====
1. ADD NEW EMPLOYEE
2. SHOW DETAILS
3. EDIT EXISTING DETAILS
4. RESIGN
5. EXIT
Choose an option:
```

### 1\. ADD NEW EMPLOYEE

  * Select option `1`.
  * You will be prompted to enter the employee's **name**, **email**, **location**, and **age**.
      * **Name** and **location** are mandatory.
      * **Email** must contain `@`.
      * **Age** must be a number between 18 and 60.
  * You can optionally enter **company name** and **company location**.
  * The data will be saved in a new text file in the `Employee` folder (e.g., `John Doe.txt` or `Jane Doe_ABC Corp.txt`).

### 2\. SHOW DETAILS

  * Select option `2`.
  * Enter the full file name of the employee (e.g., `John Doe.txt`).
  * The script will display all the details saved for that employee.

### 3\. EDIT EXISTING DETAILS

  * Select option `3`.
  * Enter the full file name of the employee you wish to edit.
  * The current details of the employee will be displayed.
  * You will then see options to:
      * **Edit a field**: Modify the value of an existing key (e.g., `name`, `email`, `age`).
      * **Delete a field**: Remove an existing key-value pair.
      * **Add new key-value pair**: Introduce a new piece of information for the employee.
      * **Go Back**: Exit the edit menu and save changes.
  * Changes are saved automatically when you choose to go back.

### 4\. RESIGN

  * Select option `4`.
  * Enter the full file name of the employee who is resigning.
  * If the employee is associated with a company, you'll be asked to provide a **reason for resignation**.
  * The `company_name` and `company_loc` fields will be removed from the employee's record, and the `reason` field will be added.

### 5\. EXIT

  * Select option `5` to exit the application.

-----

## Folder Structure

The script automatically creates an `Employee` folder in the same directory where the script is run. All employee data files (e.g., `employee_name.txt`) are stored within this folder.

```
.
├── employee_manager.py
└── Employee/
    ├── John Doe.txt
    ├── Jane Doe_ABC Corp.txt
    └── etc.
```
