class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def person(self):
        print(f"Hello I am {self.name} "
              f"born in {self.location} "
              f", {self.age} years old")


my_person = Person("James", 30, "India")
my_person2 = Person("Paul", 36, "Israel")
my_person3 = Person("Shawn", 76, "Israel")
my_person4 = Person("Caroline", 26, "USA")
my_person5 = Person("Hendrick", 67, "Britain")
my_person.person()
my_person2.person()
my_person3.person()
my_person4.person()
my_person5.person()
