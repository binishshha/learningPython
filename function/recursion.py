def fact (number):
    if number==0 || number==1:
        return 1
    else:
        return number*fact(number-1)

factorial=fact(5)
print(factorial)

