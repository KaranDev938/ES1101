# SUMMATION OF GP
a=int(input("enter the positive number"))
x=int(input("enter the number of terms"))
d=int(input("enter the positive number common ratio"))
j=0
for i in range(0,x):
    j+=a
    a=a*d
    print(j)
   