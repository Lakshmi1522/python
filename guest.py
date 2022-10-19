time=int(input("enter a number"))
entry=[]
exit=[]
for i in range(time):
    en=int(input("enter the number"))
    entry.append(en)
print(entry)
for i in range(time):
    ex=int(input("enter the number"))
    exit.append(ex)
print(exit)
count=0
guests=[]
for i in range(time):
    count=count+entry[i]-exit[i]
    guests.append(count)
print(guests)
print(max(guests))
