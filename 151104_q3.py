class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"{self.name} (ID: {self.employee_id}), Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_salary_expenditure(self):
        total = sum(emp.salary for emp in self.employees)
        print(f"Total salary for {self.department_name}: {total}")
        return total

    def display_employees(self):
        print(f"Employees in {self.department_name}:")
        for emp in self.employees:
            emp.display_details()


# Interactive code
if __name__ == "__main__":
    dept = Department("IT Department")

    while True:
        print("\n1. Add Employee\n2. Show Employees\n3. Show Total Salary\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Employee Name: ")
            eid = input("Employee ID: ")
            salary = float(input("Salary: "))
            emp = Employee(name, eid, salary)
            dept.add_employee(emp)
        elif choice == "2":
            dept.display_employees()
        elif choice == "3":
            dept.total_salary_expenditure()
        elif choice == "4":
            break
        else:
            print("Invalid option.")
