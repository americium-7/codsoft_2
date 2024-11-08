def calculator():
    N1=int(input("enter first number\n"))
    N2=int(input("enter second number\n"))
    #display operation choices
    print("choose an operation:\n")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=input()
    if choice=='1':
        result= N1 + N2
        print("Addition=",result)
    elif choice=='2':
        result=N1-N2
        print("subraction=",result)
    elif choice=='3':
        result=N1*N2
        print("multipication:",result)
    elif choice=='4':
        if N2 !=0:
            result=N1/N2
            print("division:",result)
        else:
            print("error")
    else:
        print("invalid choice") 
calculator()
