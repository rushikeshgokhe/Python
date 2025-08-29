a=int(input("Enter the marks of a"))
b=int(input("Enter the marks of b"))
c=int(input("Enter the marks of c"))
per=(a+b+c)/300*100
if a>=40 and b>=40 and c>=40 :
    if per>=50:
        print("passed:",per)
    else:
        print("failed",per)
else:
    print("failed in one or two :")
    
