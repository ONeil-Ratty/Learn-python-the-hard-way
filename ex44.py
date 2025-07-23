## implicit inhertitance

class parent(object):
    def implicit(self):
        print("implicit parent")

class child(parent):
    pass


dad = parent()
son = child()

dad.implicit()
son.implicit()

## Override explicity 

class Parent(object):

    def overide(self,name):
        self.name = name
        print(name)

class Child(Parent):
    
    def overide(self,name):
        self.name = name
        print(name)

dad = Parent()
son = Child()

dad.overide("Dad")
son.overide("Son")

## Altered before or After

class Parent(object):
    def altered(self):
        print("parent altered()")

class Child(Parent):
    def altered(self):
        print("Child before parent altered()")
        super(Child,self).altered()
        print("Child after parent altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()