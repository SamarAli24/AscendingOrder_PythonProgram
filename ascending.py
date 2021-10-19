n1 = float(input("Enter first number = "))
n2 = float(input("Enter second number = "))
n3 = float(input("Enter third number = "))
if(n1<n3 and n1<n2 and n2<n3 ):
    print(n1 , "<" , n2 , "<" , n3)
    
elif(n1<n3 and n1<n2 and n3<n2):
    print(n1 , "<" , n3 , "<" , n2)

elif(n1>n3 and n2>n3 and n2<n1):
    print(n3 ,"<" ,n2 ,"<", n1)

elif(n1>n3 and n2>n3 and n2>n1):
    print(n3 , "<" , n1 , "<" , n2)

elif(n1>n2 and n1>n3 and n3>n2):
    print(n2 , "<" , n3 , "<" , n1)

elif(n1>n2 and n1>n3 and n2>n3):
    print(n3 ,"<" , n2 , "<" , n1)
