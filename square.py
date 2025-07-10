l=[]
l2=[]
limit=int(input("enter the limit:"))
for i in range(limit):
    x=int(input("enter a number:"))
    l.append(x)
print(l)
for i in l:
        l2.append(i*i)
print(l2)