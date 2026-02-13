class person( object ):
    def __init__(self, name, Idnumber):
        self.name=name
        self.Idnumber=Idnumber
    def display(self):
        print(self.name)
        print(self.Idnumber)
class employee(person):
    def __init__(self, name, Idnumber, salary, post):
        self.salary=salary
        self.post=post
        person.__init__(self, name, Idnumber)
a=employee("Rahul", 43543543, 1000000, "intern")
a.display()