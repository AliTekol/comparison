while True:
    try:
        a=int(input("Enter number A (Enter another if done) :"))
        b=int(input("Enter number B (Enter another if done) :"))
        if a>b:
            print("A is bigger than B\n")
        elif a<b:
            print("B is bigger than A\n")
        else:
            print("A and B are equal\n")
    except ValueError:
            exit()



    
