#strfunctions and conditionslas
sent = input("Enter a sentence: ")
if sent.startswith("is"):
    print(sent)
else:
    symbol = "is"
    new = sent.replace(symbol, "was")
    print("Replacing is with was:", new)

#greatest of 3 numbers
first = int(input("First: "))
second = int(input("Second: "))
third = int(input("Third: "))

if first >= second and first >= third:
    print("First is largest")
elif second >= first and second >= third:
    print("Second is largest")
else:
    print("Third is largest")

#checking odd or even
a = int(input("Enter a number: "))
if a % 2 == 0:
    print("EVEN")
else:
    print("ODD")

