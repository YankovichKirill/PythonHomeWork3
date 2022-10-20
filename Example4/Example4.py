s = ""
n = int(input("Enter a number to convert decimal to binary:\n"))
while n != 0:
    s = str(n%2) + s
    n //= 2
print(s)