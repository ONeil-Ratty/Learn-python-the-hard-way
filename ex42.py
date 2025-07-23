
## Animal is-a object
class Animal(object):
    pass

## Dog is-a object
class Dog(Animal):
    def __init__(self, name):
        ## Dog has a name of some kind
        self.name = name

## Car is-a object
class Cat(Animal):
    
    def __init__(self,name):
        self.name = name

## person is-a object
class Person(object):
    
    def __init__(self,name):

        ## person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None


## employee is-a object
class Employee(Person):

    def __init__(self,name,salary):
        ## ?? hmm what is this strange magic?
        super(Employee,self).__init__(name)
        ## Employee has a salary
        self.salary = salary


## Fish is a object
class Fish(object):
    pass

## Salmon is a object
class Salmon(Fish):
    pass

##  Halibut is a object
class Halibut(Fish):
    pass

## rover is-dog
rover = Dog("Rover")

## satab is-cat
satan = Cat("Satan")

## mary is-person
mary = Person("Mary")

## mary has-a cat named satan
mary.pet = satan

## frank is-a employee
frank = Employee("Frank",12000)

## frnak has a pet named rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()