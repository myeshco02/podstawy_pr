#Write a program that prints the first twenty words
#of the Fibonacci sequence.
#The sequence is defined as follows:
#the first term is equal to 0,
#the second is equal to 1,
#each subsequent term is the sum of the previous two.


f0 = 0 #1. liczba ciagu
f1 = 1 #2. liczba ciagu

for x in range(20):
    print(f0, end=' ') 
    fn = f0 + f1 #n-ty wyraz ciągu to suma dwóch poprzednich (wyjsciowo 1 i 2)
    f0 = f1 # 1. wyraz ciągu dostaje wartość następnego itd.
    f1 = fn # 2. wyraz ciągu dostaje wartość następnego itd.
