inp=int(input("Insert a number:"))
x = 1
y = inp
for i in range(0,inp):
    y = inp - i
    x = x * y
print(x)
