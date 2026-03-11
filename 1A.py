num1=float(input("enter 1st number"))
num2=float(input("enter 2nd number"))
print("\nchoose operations")
print("1-add")
print("2-subtraction")
print("3-multiplication")
print("4-divide")
choice=int(input("enter your choice(1-4)"))
if choice==1:
   print("result:",num1+num2)
elif choice==2:
    print("result:",num1-num2)
elif choice==3:
    print("result:",num1*num2)
elif choice==4:
    if num2!=0:
      print("result:",num1/num2)
    else:
      print("error!division by zero is not allowed")
else:
    print("invlaid choice")
     
