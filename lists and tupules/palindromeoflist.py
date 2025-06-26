words1 = ['1', 'madam', '1']
words2 = ['1', 'madam', '1']

new = words2.copy()
new.reverse()

if new == words1:
    print("Palindrome")
else:
    print("Not a Palindrome")
