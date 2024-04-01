def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
x=int(input("Enter the x: "))
y=int(input("Enter the y: "))
output=power(x,y)
print("the answer is : ",output)