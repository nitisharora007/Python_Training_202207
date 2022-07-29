

'''
    Umbrella objects -> call the methods associated with it

# One way to import is
import Umbrella
a = Umbrella.A()

#2nd way to import is
from Umbrella import A
a = A()
'''

from cmath import cos
import statistics
from Umbrella import Umbrella

# Create the object
ub = Umbrella("Blue", "XL")

# Object, we call the open method
ub.open()
#ub.__expandUmbrella()   # won't work as __ method is private method

'''
    Result class => our numbers  => result is out => percentile => average of all students, 
                    cut-off, what the scores of other students, 

'''

# Exam => Percentile of your marks scored
# You only know your marks
# 1000 students appeared in exam
# position => percentile => (your_marks * 100 / total of all students)
# 
import statistics


from Result import Result

rs = Result([10, 20, 30, 40, 32])

# Dipika => 23 
#print(f"Result: {rs.calc_percentile(23)}")

# Rahul => 46
#print(f"Result: {rs.calc_percentile(46)}")

#print(f"Result: {rs.calc_percentile(37)}")

print(type(rs))
ls = [1,2,3,8]
#print(type(ls))


print(rs)
print(rs.__str__())

# Private => starts with __ => Custom classes
# Magic => starts with __ and ends with __  => optional 
        # if you want to change the behavior, then you can define it 

# <result .. <memory>