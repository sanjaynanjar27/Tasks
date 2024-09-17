class Person(object):

    # __init__ is known as the constructor
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def display(self):
        print(self.name)
        print(self.number)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.number))


# child class
class Employee(Person):
    def __init__(self, name, number, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, number)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.number))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
a.display()
a.details()