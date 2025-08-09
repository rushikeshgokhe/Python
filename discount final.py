pen=int(input("pen:"))
pencil=int(input("pencil:"))
scale=int(input("scale:"))
total=pen+pencil+scale
print("Total Prize=",total)
dis=(pen+pencil+scale)*10/100
print("Discount prize=",dis)
fin=(total-dis)
print("Final prize=",fin)


