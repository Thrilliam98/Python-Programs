age = 5
print(" The Value of Age = ", age)
print(" The Variable Age is Located in ", id(age))

def changeage(x):
    x = x+1
    print(" The Value of Age When Passed to Function is ", x)
    print(" The Memory Location of ge when passed to function is ",id(x))

changeage(age)

print(" The value of age after the function call ",age)
print(" The Memory Location of age after the function call is ", id(age))
