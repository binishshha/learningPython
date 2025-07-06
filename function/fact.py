number= int(input("Enter a number:"))
factorial=1

if number<0:
    print("We don't have the factorial of negative number")
else:
    for i in range(1,number+1):
        factorial *= i

print(factorial)