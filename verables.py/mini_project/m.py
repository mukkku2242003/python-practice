# import student
# student.show_student("mukesh kumar",75)
# student.check_results(75)
# import calculator as cal

# print(cal.add(50, 30))
# print(cal.subtract(50, 30))
# print(cal.multiply(5, 6))
# print(cal.divide(100, 5))
# import math 
# import random 
# import datetime
# import os

# print("squre root",math.sqrt(100))
# print("random number ",random.randint(1,100))
# print("date time :",datetime.date.today())
# print("os:",os.getcwd())

# file = open("data.txt", "w")

# file.write("Hello Mukesh Kumar")

# file.close()
# file = open("data.txt", "r")

# content = file.read()

# print(content)

# file.close()

# with open("student.txt", "w") as file:
#     file.write("Name: Mukesh Kumar\n")
#     file.write("Marks: 85\n")
#     file.write("Result: Pass\n")

# with open("student.txt", "r") as file:
#     content = file.read()
#     print(content)
# with open("student.txt","a") as file:
#     file.write("name:mukku jii\n")
#     file.write("b tech ai \n")
# with open("student.txt","r") as file:
#     content = file.read()
#     print(content)

# with open("student.txt","w") as file:
#     file.write("name : mukesh kumar\n")
#     file.write("branch : AIML \n")
# with open("student.txt","a") as file :
#     file.write("sallary : 35000 \n")
# with open("student.txt","r") as file :
#     for line in file:
#        if "sallary" in line:
#         parts =line.split(":")
#         sallary=parts[1].split()
#     print(sallary)
# with open("employee.txt","w") as file:
#     file.write("name : mukesh kumar \n")
#     file.write("department : ENGINEER \n")
#     file.write("sallary : 35000 \n")
# with open("employee.txt","r") as file:
#     for line in file: 
#         if "department" in line :
#             parts=line.split(":")
#             department=parts[1].strip()
#             print(department)

# import csv

# with open("employees.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Name", "Salary", "Department"])
#     writer.writerow(["Mukesh", 35000, "Accounts"])
#     writer.writerow(["Rahul", 45000, "Sales"])
#     writer.writerow(["Amit", 50000, "IT"])
#     writer.writerow(["Chandan", 60000, "AI"])

# total_salary = 0


# with open("employees.csv", "r") as file:
#     reader = csv.reader(file)

#     next(reader)

#     for row in reader:
      
#         salary = int(row[1])
#         total_salary=total_salary + salary
#     print("total salary,",total_salary)


# import csv

# with open("employees.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Name", "Salary", "Department"])
#     writer.writerow(["Mukesh", 35000, "Accounts"])
#     writer.writerow(["Rahul", 45000, "Accounts"])
#     writer.writerow(["Amit", 50000, "IT"])
#     writer.writerow(["Chandan", 60000, "Accounts"])
#     writer.writerow(["mukku",70000,"accounts "])


# with open("employees.csv", "r") as file:
#     reader = csv.reader(file)

#     next(reader)

#     for row in reader:
#         name = row[0]
#         salary=int(row[1])
#         department = row[2]

#         if department == "Accounts":
#           print(name,salary,department)


# import csv
# with open("employee.csv","w","new_line=") as file :
#     writer=csv.writer(file)

#     writer.writerow(["Name","Salary","Department"])
#     writer.writerow(["Mukesh","35000","Accounts"])
#     writer.writerow(["Rahul","45000","Sales"])
#     writer.writerow(["Amit","50000","IT"])
#     writer.writerow(["Chandan","60000","AI"])

# with open ("employee.csv","r") as file :
#     reader=csv.reader(file)





# import csv

# with open("employees.csv", "w", newline="") as file:
#     writer = csv.writer(file)

#     writer.writerow(["Name", "Salary", "Department"])
#     writer.writerow(["Mukesh", 35000, "Accounts"])
#     writer.writerow(["Rahul", 45000, "Sales"])
#     writer.writerow(["Amit", 50000, "IT"])
#     writer.writerow(["Chandan", 60000, "AI"])


# with open("employees.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         if row["Department"] == "Accounts":
#             print(row["Name"], row["Salary"], row["Department"])






# import csv

# employees = [
#     {"Name": "Mukesh", "Salary": 35000, "Department": "Accounts"},
#     {"Name": "Rahul", "Salary": 45000, "Department": "Sales"},
#     {"Name": "Amit", "Salary": 50000, "Department": "IT"},
#     {"Name": "Chandan", "Salary": 60000, "Department": "AI"},
# ]

# with open("employees.csv", "w", newline="") as file:
#     fieldnames = ["Name", "Salary", "Department"]

#     writer = csv.DictWriter(file, fieldnames=fieldnames)

#     writer.writeheader()

#     writer.writerows(employees)

# with open("employees.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row["Name"], row["Salary"], row["Department"])

# import csv

# employees = [
#     {"Name": "Mukesh", "Salary": 35000, "Department": "Accounts"},
#     {"Name": "Rahul", "Salary": 45000, "Department": "Sales"},
#     {"Name": "Amit", "Salary": 50000, "Department": "IT"},
#     {"Name": "Chandan", "Salary": 60000, "Department": "AI"},
# ]

# with open("employees.csv", "w", newline="") as file:
#     fieldnames = ["Name", "Salary", "Department"]

#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(employees)


# total_salary = 0
# high_salary_employees = []

# with open("employees.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         name = row["Name"]
#         salary = int(row["Salary"])
#         department = row["Department"]

#         total_salary = total_salary + salary

#         if salary >= 50000:
#             high_salary_employees.append({
#                 "Name": name,
#                 "Salary": salary,
#                 "Department": department
#             })


# with open("high_salary_employees.csv", "w", newline="") as file:
#     fieldnames = ["Name", "Salary", "Department"]

#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(high_salary_employees)


# print("Total Salary:", total_salary)
# print("High salary employees file created")


# import json

# employee = {
#     "name": "Mukesh Kumar",
#     "salary": 35000,
#     "department": "Accounts"
# }

# with open("employee.json", "w") as file:
#     json.dump(employee, file)

# with open("employee.json", "r") as file:
#     data = json.load(file)

# print("Name:", data["name"])
# print("Salary:", data["salary"])
# print("Department:", data["department"])

# import json

# employees = [
#     {"name": "Mukesh", "salary": 35000, "department": "Accounts"},
#     {"name": "Rahul", "salary": 45000, "department": "Sales"},
#     {"name": "Chandan", "salary": 60000, "department": "AI"}
# ]

# with open("employees.json", "w") as file:
#     json.dump(employees, file, indent=4)

# cc
# for employee in data:
#     if employee["salary"] >= 50000:
#         print(employee["name"], employee["salary"], employee["department"])

# import json

# employe={
#     "name": "Chandan",
#     "salary": 40000,
#     "department": "Python"
# }

# with open("employe.json","w") as file:
#     json.dump(employe,file,indent=4)
# with open("employe.json", "r") as file:
#  data = json.load(file)


# data["salary"]=60000
# data["department"]="aiml engeenier"
# data["status"]="active"
# with open("employe.json", "w") as file:
#     json.dump(data, file, indent=4)
# print("Salary updated successfully")
# import json
# employees = [
#     {"name": "Mukesh", "salary": 35000, "department": "Accounts"},
#     {"name": "Rahul", "salary": 45000, "department": "Sales"},
#     {"name": "Chandan", "salary": 60000, "department": "Python"}
# ]

# with open("employees.json","w") as file:
#       json.dump(employees,file,indent=4)
# with open("employees.json", "r") as file:
#    data = json.load(file)
# for employees in data:
#     if employees["name"] == "Chandan":
#         employees["department"] = "aiml eng"
# new_employees={"name": "Amit", "salary": 50000, "department": "IT"}
# data.append(new_employees)

# with open("employees.json", "w") as file:
#     json.dump(data, file, indent=4)
# print("new employee add")
# print("department  updated")


# import json

# employees = [
#     {"name": "Mukesh", "salary": 35000, "department": "Accounts"},
#     {"name": "Rahul", "salary": 45000, "department": "Sales"},
#     {"name": "Amit", "salary": 50000, "department": "IT"}
# ]

# with open("employees.json", "w") as file:
#     json.dump(employees, file, indent=4)

# with open("employees.json", "r") as file:
#     data = json.load(file)

# for employee in data:
#     print("Name:", employee["name"])
#     print("Salary:", employee["salary"])
#     print("Department:", employee["department"])
#     print("----------------")
# while True:
#     print("\nEmployee Management System")
#     print("1. Add Employee")
#     print("2. Show Employees")
#     print("3. Update Salary")
#     print("4. Delete Employee")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         print("Add Employee selected")

#     elif choice == "2":
#         print("Show Employees selected")

#     elif choice == "3":
#         print("Update Salary selected")

#     elif choice == "4":
#         print("Delete Employee selected")

#     elif choice == "5":
#         print("Program closed")
#         break

#     else:
# #         print("Invalid choice")


# import json

# employees = [
#     {"name": "Mukesh", "salary": 35000, "department": "Accounts"},
#     {"name": "Rahul", "salary": 45000, "department": "Sales"}
# ]

# with open("employees.json", "w") as file:
#     json.dump(employees, file, indent=4)


# def add_employee():
#     name = input("Enter name: ")
#     salary = int(input("Enter salary: "))
#     department = input("Enter department: ")

#     employee = {
#         "name": name,
#         "salary": salary,
#         "department": department
#     }

#     with open("employees.json", "r") as file:
#         data = json.load(file)

#     data.append(employee)

#     with open("employees.json", "w") as file:
#         json.dump(data, file, indent=4)

#     print("Employee added successfully")


# while True:
#     print("\nEmployee Management System")
#     print("1. Add Employee")
#     print("2. Show Employees")
#     print("3. Update Salary")
#     print("4. Delete Employee")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_employee()

#     elif choice == "2":
#         print("Show Employees selected")

#     elif choice == "3":
#         print("Update Salary selected")

#     elif choice == "4":
#         print("Delete Employee selected")

#     elif choice == "5":
#         print("Program closed")
#         break

#     else:
#         print("Invalid choice")



# def get_salary():
#     while True:
#         try:
#             salary = int(input("Enter salary: "))

#             if salary > 0:
#                 return salary
#             else:
#                 print("Salary must be greater than 0")

#         except ValueError:
#             print("Invalid salary. Please enter numbers only.")


# salary = get_salary()

# print("Salary saved:", salary)




import json   # JSON file read/write karne ke liye module import kiya

FILE_NAME = "employees.json"   # JSON file ka naam ek variable me store kiya


# Ye function JSON file se employee data read karega
def load_employees():
    try:
        # employees.json file ko read mode me open kar rahe hain
        with open(FILE_NAME, "r") as file:
            data = json.load(file)   # JSON data ko Python list/dictionary me convert karta hai
            return data              # data ko function ke bahar return karta hai

    except FileNotFoundError:
        # Agar file exist nahi karti, to empty list return karo
        return []

    except json.JSONDecodeError:
        # Agar JSON file corrupt/kharab hai, to program crash nahi hoga
        print("JSON file corrupt hai. Empty data se start kar rahe hain.")
        return []


# Ye function employee data ko JSON file me save karega
def save_employees(data):
    # employees.json file ko write mode me open kar rahe hain
    with open(FILE_NAME, "w") as file:
        # Python list/dictionary ko JSON file me save kar rahe hain
        json.dump(data, file, indent=4)


# Ye function salary input ko safe banata hai
def get_salary():
    while True:   # Jab tak valid salary nahi milegi, loop chalta rahega
        try:
            # User se salary input lekar integer me convert kar rahe hain
            salary = int(input("Enter salary: "))

            # Salary positive honi chahiye
            if salary > 0:
                return salary   # Valid salary mil gayi, function se return kar do
            else:
                print("Salary must be greater than 0")

        except ValueError:
            # Agar user abc ya wrong input de, to ye message show hoga
            print("Invalid salary. Please enter numbers only.")


# Ye function new employee add karega
def add_employee():
    name = input("Enter name: ")        # Employee ka naam input
    salary = get_salary()              # Safe salary input
    department = input("Enter department: ")  # Department input

    # New employee ka dictionary banaya
    employee = {
        "name": name,
        "salary": salary,
        "department": department
    }

    data = load_employees()   # Purana data JSON file se read kiya
    data.append(employee)     # New employee list ke end me add kiya
    save_employees(data)      # Updated data JSON file me save kiya

    print("Employee added successfully")


# Ye function saare employees show karega
def show_employees():
    data = load_employees()   # JSON file se data read kiya

    # Agar data empty hai
    if len(data) == 0:
        print("No employees found")
    else:
        # Har employee ko one by one print karna
        for employee in data:
            print("Name:", employee["name"])
            print("Salary:", employee["salary"])
            print("Department:", employee["department"])
            print("----------------")


# Ye function employee ki salary update karega
def update_salary():
    name = input("Enter employee name to update salary: ")  # Jiska salary update karna hai
    new_salary = get_salary()  # New salary safe input se lena

    data = load_employees()   # JSON file se data read
    found = False             # Employee mila ya nahi, iske liye flag

    # Har employee check kar rahe hain
    for employee in data:
        # lower() se case-insensitive comparison hota hai
        if employee["name"].lower() == name.lower():
            employee["salary"] = new_salary  # Salary update
            found = True                     # Employee mil gaya
            break                            # Loop stop

    # Agar employee mila hai
    if found:
        save_employees(data)  # Updated data save karo
        print("Salary updated successfully")
    else:
        print("Employee not found")


# Ye function employee delete karega
def delete_employee():
    name = input("Enter employee name to delete: ")  # Jisko delete karna hai

    data = load_employees()   # JSON file se data read
    updated_data = []         # New list jisme delete wala employee nahi hoga
    found = False             # Employee mila ya nahi

    # Har employee check karna
    for employee in data:
        # Agar employee ka name match ho gaya
        if employee["name"].lower() == name.lower():
            found = True      # Employee mil gaya, isko updated_data me add nahi karenge
        else:
            updated_data.append(employee)  # Baaki employees ko new list me add karo

    # Agar employee mila tha
    if found:
        save_employees(updated_data)  # New list JSON file me save
        print("Employee deleted successfully")
    else:
        print("Employee not found")


# Main menu loop
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Show Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")  # User se menu choice lena

    if choice == "1":
        add_employee()  # Add employee function call

    elif choice == "2":
        show_employees()  # Show employees function call

    elif choice == "3":
        update_salary()  # Update salary function call

    elif choice == "4":
        delete_employee()  # Delete employee function call

    elif choice == "5":
        print("Program closed")
        break  # Loop stop, program close

    else:
        print("Invalid choice")  # Wrong option par message