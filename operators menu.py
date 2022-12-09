num1=float(input("enter first number"))
num2=float(input("enter second number"))
op= input("enter operator[+ - * / %]")
result=0
if op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=="*":
    result=num1*num2
elif op=="/":
    result=num1/num2
elif op=="%":
    result=num1%num2
    c=num1%num2,"your number is "
else:
    print("invalid operator!!")
print(num1,op,num2,"=",result)
