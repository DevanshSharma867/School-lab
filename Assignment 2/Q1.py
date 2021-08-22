from sys import exit
num = int(input('Enter your number '))

def prime(num=num):
    result = 'Prime'
    for factor in range(2, int(num**0.5)+1):
        if num % factor == 0:
            result = 'Not prime'
            break
    return(result)


def perfect(num=num):
    temp = 0
    result = 'Not perfect'
    for factor in range(1, (num//2)+1):
        if num % factor == 0:
            temp += factor
    if num == temp:
        result = 'Perfect'
    return(result)


def twinprimes(num=num):
    result = 'Not twin prime'
    if prime(num) == 'Prime':
        if prime(num+2) == 'Prime' or prime(num-2) == 'Prime':
            result = 'Twin prime'
    return(result)

def menu(num=num):
    choice = int(input('''Write a menu based program to print the following menu:
1)Prime
2)Perfect
3)Twin Primes
4)Exit
Write separate functions for each.
'''))
    if choice == 1: print(prime())
    if choice == 2: print(perfect())
    if choice == 3: prime(twinprimes())
    if choice ==4: exit()

while True:
    menu()