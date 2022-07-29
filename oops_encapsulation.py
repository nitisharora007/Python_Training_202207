'''

OOPS - Real-world

    Encapsulation -  Important concept of OOPS which mainly deals 
                        with hiding of the data and the methods

    -> Hide the internal working of the object
    -> Expose/Provides the methods to use the object


Laptop -> ram, cpu, os, brand, keyboard
        -> how does the keyboard => q is pressed => it sends a signal to motherboard (0&1) => 
                    displayed on the screen or monitor
        q key is pressed => convert the q => 0&1 => send the signal => application => shortcut
        -> press the key => 
        
Car -> press the acc. -> Speed goes up (methods exposed)
        Internal working: Wire -> sends more fuel to the engine -> burn the fuel in engine -> speeds up the car
                                    calling few methods
                        Hidden from the object  (Private methods)

In Python:
    public methods => no special declaration

        def <methodName>(<parameters>):
            pass

            => Can be used anywhere

    private method => provide two underscores at the starting of the function name

        def __<methodName>(<parameters>):
            pass

                => Not the child can use it
                => Not allowed outside the class 

    protected method => provide one underscore at the starting of the function name
        def _<methodName>(<parameters):
            pass

                => Child class can use it from base class
                => Not outside the class
'''

class Car:

    __gear = 0
    
    def __init__(self, windows = 4):
        self.__a = 0
        self.max_speed = 0
        self.windows = windows
  
    def reset(self):

        self.__gear = 0
        self.max_speed = 0

    def print_state(self):
        print(f"Current gear: {self.__gear}, MaxSpeed: {self.max_speed}, Windows: {chevy.windows}")

    def press_acc(self):
        
        if self.__gear == 0:
            self.max_speed = 0
        
        if self.__gear > 4:
            self.__gear = 5

        self.__gear = self.__gear + 1
        self.max_speed = self.__gear * 30

        #self.__fuel_burnt = self.__fuel_burnt - (self.gear*2)

    def press_break(self):

        if self.__gear == 0:
            self.max_speed = 0

        if self.__gear < 0:
            self.__gear = 0

        self.__gear = self.__gear - 1
        self.max_speed = self.__gear * 30

    def __internal_gear(self):
        print("Internal gear changes")

    

chevy = Car()           # Created the object

chevy.press_acc()       #
chevy.print_state()

chevy.print_state()
chevy.print_state()
chevy.print_state()

chevy.press_acc()
chevy.print_state()

#chevy.__internal_gear()

'''
chevy.press_break()
print(f"Current gear: {chevy.gear}, MaxSpeed: {chevy.max_speed}")

chevy.press_acc()
print(f"Current gear: {chevy.gear}, MaxSpeed: {chevy.max_speed}")

chevy.press_break()
print(f"Current gear: {chevy.gear}, MaxSpeed: {chevy.max_speed}")


Design a car class, which has the attributes, speed, gear
    
    Maths => average of marks
                    sum, length 
                    avg = sum(list)/len(list)

    Create a class named Maths, average, mean, meadian

            sum
            avg = sum/len
            perc =  what/total * 100
            median = sum /len 

            20% of 100 => 20/100 * 100
            what% of <total> 

    Umbrella => Open & Close => button pressed => 

    class Umrella:

        def __init__():
            pass

        lock => hook that holds the wire => frees up the lock =>  wire is expand => certain point with force => open the umbrella 
        def press_button():

            self.__open_lock()
            self.__expand_wire()



'''

