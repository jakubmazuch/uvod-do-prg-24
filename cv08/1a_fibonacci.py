def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        print(a, end=", ")
        a, b = b, a+b


x = int(input("Zadejte počet členů Fibonacciho posloupnosti: "))
fibonacci(x)
