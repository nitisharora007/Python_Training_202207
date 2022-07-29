'''
    Inheritance => 
        Important concept of the OOPS world.

    Relationship between the parent & the child

    Parent => Inherit some features from the parents & we do have our own features

    Any class which wants to inherit the features from another class, then it becomes the concept
    of inheritance

    Class A wants to use features from Class B

    Class A => Child class wants to inherit from the Class B => Parent Class


    Syntax:

        class <ParentClassName>:
            pass

        class <ChildClassName>(<ParentClassName>):
            pass

'''

class Parent:

    def __init__(self):
        self.a = 10
        print("In the parent class")

    def display(self):
        print(f"In the class A: {self.a}")


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("In child class")

#prnt = Parent()
#prnt.display()

#chld = Child()
#chld.display()




from GermanSh import GermanSh

gs = GermanSh("blue", 10)
print(f"Features: Dog is {gs.color} in color having {gs.num_teeths} teeth, {gs.jump_height}")

gs.jump()
gs.bark()


'''
    Private, Protected and Public
    Multiple/Multilevel

class PitBull(Dog):

    def __init__(self, color, num_teeths):
        super().__init__(color, num_teeths)
        # get the parent(s), then invoke the init method
        # Dog.__init__(color, num_teeths)

    def walk(self):
        print("Dog can walk")


pb = PitBull("darkgrey", 5)
print(f"Features: Dog is {pb.color} in color having {pb.num_teeths} teeth")
print(f"Features: Dog is {gs.color} in color having {gs.num_teeths} teeth")
gs.bark()
gs.jump()
pb.bark()
pb.walk()

'''


