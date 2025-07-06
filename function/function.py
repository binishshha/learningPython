def fact (number):
    factorial=1
    if number<0:
        print("We don't have the factorial of negative number")

    for i in range(1,number+1):
        factorial *= i
    
    return factorial

factorial=fact(5)
print(factorial)

