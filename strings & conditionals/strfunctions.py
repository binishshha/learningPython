# Find position of first "a"
inp = input("Enter a string: ")
print(inp.find("a"))

# Masking email address
email = input("Enter an email address: ")
symbol = email.find("@")

username = email[:symbol]
domain = email[symbol:]
maskedmail = username[0] + "*" * (len(username) - 2) + username[-1] + domain

print("Masked email:", maskedmail)
