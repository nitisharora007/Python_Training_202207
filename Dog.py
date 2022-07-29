class Dog:

    def __init__(self, color, num_teeths):
        self.color = color                  # Attribute 1 
        self.num_teeths = num_teeths        # Attribute 2
        print("   ")

    # Method 1
    def bark(self):
        print("Dog is barking")

    # Method 2
    def trained(self):
        print(f"Dog is trained")
