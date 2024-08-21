class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def xprint(self):
        print(self.firstname,self.lastname)

x=Person("shadab","ansari")
x.xprint()

class Child(Person):
    def __init__(self, fname, lname,year):
     Person.__init__(self, fname, lname)
     self.graduationyear = year
    def welcome(self):
     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x=Child(f"gopal","kumar","the graduation year is{2039}")
x.xprint()
x.welcome()
# print(x.graduationyear)
