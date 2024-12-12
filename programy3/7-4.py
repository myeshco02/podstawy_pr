from calculations import count_letter

# Liczenie wystąpień litery w tekście
text = "You never get a second chance to make a first impression"
letter = 'e'
count = count_letter(text, letter)
print(f"The number of letter '{letter}': {count}")
