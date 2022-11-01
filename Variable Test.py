anotherVariable = 100

def variableTest():
    global firstVariable
    firstVariable = 10
    secondVariable = 20
    return firstVariable * secondVariable

print(variableTest())
print(firstVariable)
