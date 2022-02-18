#calcula a sequencia de collatz para o número 
n = 1023
while n > 1:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1

        print(n)