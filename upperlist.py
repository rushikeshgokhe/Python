a=[[10,20,30],[40,50,60],[1,2,3]]
#b=[[6,7,8],[9,10,11],[12,13,14]]
#c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3,1):
    for j in range(0,3,1):
        if j<i:
            print("0",end="")
        else:
            print(a[i][j],end="")
    print()        
        
         
