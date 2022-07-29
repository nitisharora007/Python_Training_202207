'''
    Umbrella
        -> attributes: color
        -> size

    -> open
    -> close
'''

class Umbrella:

    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.__isOpen = False

    # Private methods
    def __signalsent(self):
        print("Signal sent")

    # Private methods
    def __expandUmbrella(self):
        print("Umbrella is expanding")

    # Private methods
    def __shrinkUmbrella(self):
        print("Umbrella is shrinking")

    # Public methods
    def open(self):

        print("Opening the umbrella")
        self.__signalsent()
        self.__expandUmbrella()

    def close(self):
        print("Closing the umbrella")

class A:

    def __init__(self) -> None:
        pass

    def some_fun(self):
        print("some function")