#There are coins of 1, 2 and 5 Polish Zlotys (PLN).
#Write a program showing any amount (natural number)
#read from the keyboard with as few coins as possible.

amount = int(input('Amount of PLN: '))
original = amount

fivepln = 0
twopln = 0
onepln = 0

for x in range(amount // 5): # sprawdza ile 5 sie zmiesciw danej liczbie
    fivepln += 1
    amount -= 5
    
for x in range(amount // 2): # sprawdza ile dwojek miesci sie w danej liczbie
    twopln += 1
    amount -= 2

onepln = amount # reszte ktore sie nie podzielilo przez 5 i 2 to 1 czy cos

print(f'The amount of PLN {original} in coins:')
print(f'5 PLN coins: {fivepln}')
print(f'2 PLN coins: {twopln}')
print(f'1 PLN coins: {onepln}')
