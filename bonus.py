g=input(" enter the grade")
s=int(input("enter the salary"))
if g=='a':
    if s<=10000:
        b=s*0.07
    else:
        b=s*0.05
else:
    if s<10000:
        b=s*0.12
    else:
        b=s*0.10
print(b)
