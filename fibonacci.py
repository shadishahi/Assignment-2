def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("'Please enter your number: "))
print("fibonacci sequence :")
for i in range(n):
    print(fibonacci(i))
