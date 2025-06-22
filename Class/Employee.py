class Employee:
    employeeName="Hanumant"
    employeeAge=22
    employeeSalery=1200

# Conctructor will get invoked first

    def __init__(self):
        print("***** I am default Constructor *****")
        self.employeeName='Pranay'
        self.employeeAge=34
        self.employeeSalery=99

    def getEmployeeDetails(self):
        print("Employee Name ::",self.employeeName)
        print("Employee Age ::",self.employeeAge)
        print("Employee Salary ::", self.employeeSalery)
