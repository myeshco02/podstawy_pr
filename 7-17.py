def f(palindrome):
    return palindrome == palindrome[::-1]

print(f("radar"))     # wynik: True
print(f("12-11-21"))  # wynik: True
print(f("book"))      # wynik: False
