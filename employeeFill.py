class Employee:
        def __init__(self, name, shiftNumber, HPR):
            self.name=name
            self.shiftNumber=shiftNumber
            self.HPR=HPR
        def displayEmployee(self):
            print("Name:", self.name, ", Shift Number:", self.shiftNumber, ", HPR:", self.HPR)
e1=Employee("Susan Meyers", "1", "$12.50")
e2=Employee("Mark Jones", "3", "$12.50")
e3=Employee("Joy Rogers", "2", "$12.50")


e1.displayEmployee()
e2.displayEmployee()
e3.displayEmployee()
