def f(text):
    return '-'.join(text)

print(f("Univesity"))  # wynik: "U-n-i-v-e-r-s-i-t-y"
print(f("UE"))         # wynik: "U-E"
print(f("x"))          # wynik: "x"
print(f(""))           # wynik: ""
