m=int(input("Enter the marks of maths:"))
e=int(input("Enter the marks of english:"))
c=int(input("Enter the marks of compter:"))
percentage=(m+c+e)/300*100
if m>40:
    if e>40:
        if c>40:
            if percentage>50:
                print("passed:",percentage)
            else:
                 print("failed:",percentage)
        else:
             print("failed3:",percentage)
    else:
        print("Failed2=",percentage)
else:
    print("failed1=",percentage)
