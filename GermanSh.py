from Dog import Dog

class GermanSh(Dog):

    def __init__(self, color, num_teeths):
        super().__init__(color, num_teeths)
        #Dog.__init__(self, color, num_teeths)
        self.jump_height = 20       # attribute

    # Method   
    def jump(obj):
        print(f"{obj.color} color Dog can jump to {obj.jump_height} m")

        # obj = > All the attributes of parent class + its own attributes
        #    attributes => color, num_teeths + jump_height
        #    method => All the methods of parent class + its own methods
        #              => bark() & trained() + jump

