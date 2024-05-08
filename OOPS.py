class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    def getsalary(self):
        return self.salary
    
rohan =Employee( "Rohan" ,"89") 
print(rohan.salary)
print(rohan.name)