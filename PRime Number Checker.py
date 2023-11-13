
def prime_checker(number):
    esPrimo = True
    for i in range(2, number):
        if number % i == 0:
            esPrimo = False
    if esPrimo:
        print("Es un numero primo!")
    else:
        print("NO es un numero primo!")

n = int(input("Check this number: "))
prime_checker(number = n)

