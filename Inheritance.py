# parent class
class Animal:
    def speak(self):
        print("Animals can make sounds")

# child class
class dog(Animal):
    def bark(self):
        print("Dog barks: woof! woof!")


# create object
dog1 = dog()
dog1.speak()
dog1.bark()


# single inheritance

class parent:
    def show_parents(self):
        print("I am the parent")

class child(parent):
    def show_child(self):
        print(" i am the child")

obj = child()
obj.show_parents()
obj.show_child()

# multiple inheritance

class father:
    def skill1(self):
        print("good at driving")

class mother:
    def skill2(self):
        print("good at cooking")

class child(father,mother):
    def skill3(self):
        print("good at studying")

obj = child()
obj.skill1()
obj.skill2()
obj.skill3()


# multilevel inheritance

class grandparent:
    def greet(self):
        print("hello from grandparent")

class parent(grandparent):
    def info(self):
        print("hello from parent")

class child(parent):
    def message(self):
        print("hello from child")

obj = child()
obj.greet()
obj.info()
obj.message()

# hierarchical inheritance

class Animal:
    def sound(self):
        print("animals make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()