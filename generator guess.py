def guesser():
    #random generator....
    import random
    a=int(input("first range:"))
    b=int(input("second range:"))
    answer=random.randint(a,b)
    guess=int(input("guess the number between the range u chose"))
    i=1
    if guess==answer:
        print("U guessed it right first time")
    else:
        while guess!=answer:
            print("try again")
            guess=int(input())
            i+=1
            if i>=5:
                print("sorry u didnt get the answer")
                break
            else:
                if guess== answer:
                    print("U guessed it right in",i,"chance")

try:
    num=int(input("enter a no. to divide: "))
    denom=int(input("no. to be divided by: "))
    result=num/denom
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero")
except Exception as e: 
    print(e)
    print("something went wrong :((")
else:
    print(result)
finally:
    print("will always execute ")