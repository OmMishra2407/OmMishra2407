def calc():
    god1 = float(input("Enter 1st No:"))
    god2 = float(input("Enter 2nd No:"))
    god3 = float(input("Enter 3rd No:"))
    print('1.Addition\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\n6.Exponention')
    inputChoice = input()
    if inputChoice == "1":
        print(god1+god2+god3)
    
    elif inputChoice == "2":
        print(god1-god2-god3) 
    
    elif inputChoice == "3":
        print(god1*god2*god3)
    
    elif inputChoice == "4":
        print(god1/god2/god3)  
    
    elif inputChoice == "5":
        print(god1%god2%god3)
    
    elif inputChoice == "6":
        print(god1**god2**god3) 


calc()      
while True:
    xy = input("Do You Want to Calculate More (y/n):")
    if xy == "n":
        break
    elif xy == "y":
        calc()