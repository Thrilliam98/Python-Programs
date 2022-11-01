def commission(price,rate):
    if price>100000:
        x= float(rate)/100*price
        return x
    else:
        print("commission = 0")

a= int(input("Enter the Sales Amount: "))
b= int(input("Enter the Commission Rate: "))

print("The Sales Commission is ", commission(a,b))
