def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def f(n):
    primes = []
    number = 2  # Zaczynamy od 2, ponieważ 2 jest pierwszą liczbą pierwszą
    
    while len(primes) < n:
        if is_prime(number):
            primes.append(number)
        number += 1
    
    return primes[-1]

print(f(1))  # wynik: 2 (pierwsza liczba pierwsza)
print(f(5))  # wynik: 11 (piąta liczba pierwsza)
print(f(10)) # wynik: 29 (dziesiąta liczba pierwsza)
