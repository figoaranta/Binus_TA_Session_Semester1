#A= int(input("Insert a number:"))
#for i in range (1 , A+1):
#    print("*" * i)


#A = int(input("Insert a number:"))
#for i in range (1 , A+1):
#    print(" " * (A - i),"*" * i)


#A = int(input("Insert a number:"))
#for i in range (1 , A+1):
#    print("*" * ((A+1) - i))


#A = int(input("Insert a number:"))
#for i in range (1 , A+1):
#    print("*" * ((A-1) + i))

#x = 5
#while x >=1:
#    print((" " * (5-x)) , ("*" * x))
#    x = x-1

x= int(input("insert a nnumber:"))
i=1
j=x
k=1
while k<=x:
    print(" "*j,"*"*i)
    i=i+2
    j=j-1
    k=k+1

n = 5
stars = [('*' + '**'*i).center(2*n + 1) for i in range(n)]

print('\n'.join(stars + stars[::-1][1:]))