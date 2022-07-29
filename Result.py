'''
    Result class => our numbers  => result is out => percentile => average of all students, 
                    cut-off, what the scores of other students
'''


class Result:

    def __init__(self, student_marks):
        self.student_marks = student_marks
        self.__sum = 0
        self.__calcsum()


    # Private method - not allowed to call outside class

    def __str__(self) -> str:
        return "Object "

    '''
        Some documentation
    '''
    def __calcsum(self):

        print(f"Calculating sum")

        for elem in self.student_marks:
            self.__sum += elem

    # Public method - allowed to call 
    def calc_percentile(self, marks):

        print(f"Sum is {self.__sum}")
        return (marks * 100 )/self.__sum