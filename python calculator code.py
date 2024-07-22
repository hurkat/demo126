print("Welcome to calculator!!")
a = int(input("add first number"))
b = int(input("add second number"))

answer = int(input("""What operation you would like to perform?? :
1. add
2. subtract
3. multiply
4. divide"""))

if answer == 1 :
    print("result : " , a + b)
elif answer == 2:
    print("result : " , a - b)
elif answer == 3:
    print("result : ", a * b)
elif answer == 4 :
    print("result : " , a / b )
else:
    print("wrong operation")
