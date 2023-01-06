# FIBONACCHI SEQUENCE
x=int(input("enter the number of terms"))
n1,n2=0,1
j=0
for i in range(1,x+1):
    j=n1+n2
    n1=n2
    n2=j
    print(n1)    
    

   