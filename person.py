class Person():
    def __init__(self,name, age, salary):
        self.age=age
        self.name=name
        self.salary=salary

    def greeting(self, guest_name):
        print("Hello " +guest_name+" my name is "+self.name)
