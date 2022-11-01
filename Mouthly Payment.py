def payment(x,y,z):
    a = (x*y*((1+y)**z))
    b = (((1+y)**z)-1)
    c = (a/b)
    return c
x= 50000
y= 0.02
z= 24
a= payment(x,y,z)
print("Loan Amount: ", x)
print("Number of Year: ", y)
print("Annual Interest Rate: ", z)
print("Your Monthly Pay is ", a)
