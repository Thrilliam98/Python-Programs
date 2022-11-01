marks =[34,54]
print("The value in marks declared outside function ", marks)
print( "The memory location of global marks", id(marks))

def changemarks(x):
    x.append(1)
    print("The value of mark when function is called", x)
    print("The memory location of marks when function is called",id(x))

changemarks(marks)

print("The value in marks after the function call",marks)
print("The memory location of marks after the function call" , id(marks))
print(type(marks))
