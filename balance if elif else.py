name = "Rushikesh"
account = 123456789
balance = 500
id = "rushikeshgokhe"
password = 1304

chr = input("Enter your id")
a = int(input("Enter the pass"))

if chr == id and a == password:
    print("welcome")
    print("Enter your choice")
    print("2: deposit:")
    print("1: withdraw:")
    print("3: check balance:")
    choose = int(input(""))

    if choose == 1:
        wd = int(input("Enter the amount to withdraw: "))
        if wd > balance:
            print("Insufficient balance")
        else:
            currentbalance = balance - wd
            print("Withdraw successful")
            print("Name:", name)
            print("Account value:", account)
            print("Current balance:", currentbalance)

    elif choose == 2:
        depo = int(input("Enter the amount to deposit: "))
        currentbalance = balance + depo
        print("Deposit successful")
        print("Name:", name)
        print("Account value:", account)
        print("Current balance:", currentbalance)

    else:
        print("Current balance:", balance)

else:
    print("Wrong password")

