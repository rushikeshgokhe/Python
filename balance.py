name="Rushikesh"
account=123456789
balance=500
print("Enter your choice")
print("2:deposit:")
print("1:withdraw:")
choose=int(input(""))
if choose==1:
    wd=int(input("Enter the amt for withdraw"))
    if wd>balance:
        print("Insufficinet balance")
    else:
          currentbalance=balance-wd
          print("withdraw successfuly")
          print("name=,name")
          print("acc vale:",account)
          print("current b:",currentbalance)
else:
    depo=int(input("Enter the amt for depo"))
    currentbalance=balance+depo
    print("deposit successfuly")
    print("name=,name")
    print("acc vale:",account)
    print("current b:",currentbalance)
    
    
