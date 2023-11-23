def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a+b
    print(a)


x = int(input("Zadejte index členu Fibonacciho posloupnosti: "))
if x >= 0:
    fibonacci(x)
else:
    print("Nemá smysl.")
