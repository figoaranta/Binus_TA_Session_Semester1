distance = int (input("Input Distance:"))
time = int (input("Input Time:"))
acceleration = int (input("input acceleration:"))

for i in range (1, time + 1):
    print("*" * int((0.5 * acceleration * i * i)/10))


velocity =  acceleration * time
if velocity <60 :
    print("The person did not go over the speed limit",velocity,"m/s")

if velocity >60 :
    print("The person went over the speed limit",velocity,"m/s")

realdistance = 0.5 * acceleration * time * time
if realdistance < distance:
    print("The person did not reached the destination",realdistance)
if realdistance> distance:
    print("The person reached the destination",realdistance)
