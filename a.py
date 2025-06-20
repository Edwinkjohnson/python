a=int(input("enter a number"))
b=int(input("enter second number"))
print("+  -  /  *")
choice=(input("enter your choice :"))
if choice=="+":
    print(a+b)
elif choice=="-":
    print(a-b)
elif choice=="/":
    print(a/b)
elif choice=="*":
    print(a*b)
else:
    print("invalid choice")