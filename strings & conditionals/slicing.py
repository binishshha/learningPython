input = input("Enter an input: ")

# Slicing syntax => string[start:end:gap]
print(input[:6])              # From index 0 to 5
print(input[2:])              # From index 2 to end
print(input[3:6])             # From index 3 to 5
print(input[:6:2])            # From index 0 to 5, every 2nd character
print(input[::2])             # Entire string, every 2nd character
print(input[1:len(input):2])  # Characters at odd indices

#Reverse Sttring
print("Reverse String:", input[::-1])

#checking palindrome
if input[0::] == input[::-1]:
    print("palindrome")
else:
    print("Not a Palindrome")

