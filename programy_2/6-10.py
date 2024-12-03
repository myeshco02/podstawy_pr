#Write a program that calculates a dog's age in dog's years.
#For the first two years, a dog's life is equal to 10.5 human years.
#After that, each dog year is equal to 4 human years

dog_age = float(input('What is yours dog age?: '))

if dog_age <= 2:
    human_age = dog_age * 10.5
else:
    human_age = 2* 10.5 + (dog_age - 2) * 4

print(f'Yours dog age in human years is:{human_age}')
