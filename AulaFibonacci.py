def fibonacci(n):
    
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)
    6
n = int(input('Escreve um número inteiro: '))

print(fibonacci(n))