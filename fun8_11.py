def min_coins(amount_to_pay):
    #wylicza minimalną liczbę monet
    coins = [5, 2, 1]
    count = 0
    for coin in coins:
        count += amount_to_pay // coin
        amount_to_pay %= coin
    return count

def sum_digits(number, even):
    #Oblicza sumę cyfr liczby na podstawie parametru 'even'
    digits = [int(d) for d in str(abs(number))]
    if even:
        return sum(d for d in digits if d % 2 == 0)
    else:
        return sum(d for d in digits if d % 2 != 0)
    
def count_negative_evens(x, y):
    """Returns the count of negative even numbers in the range <x, y>."""
    return len([n for n in range(x, y + 1) if n < 0 and n % 2 == 0])

def has_negative(n1, n2, n3):
    """Checks if at least one of the numbers is negative."""
    return n1 < 0 or n2 < 0 or n3 < 0