
func = lambda x : x/3 if x%3 == 0 else x

    ######### SIMILAR ##################

def func1(x):

    if x%3 == 0:
        return x/3
    else:
        return x

    ######### SIMILAR ##################


def func2(x):

    return x/3 if x%3 ==0 else x 


print(f" Function execution: {func(10)}, {func1(10)}, {func2(10)}")
print(f" Function execution: {func(9)}, {func1(9)}, {func2(9)}")
