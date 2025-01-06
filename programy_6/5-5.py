# Akapit do analizy
paragraph = "cat dog mouse cat rat cat mouse"

# Podział akapitu na słowa
words = paragraph.split()

# Słownik do przechowywania liczby wystąpień każdego słowa
word_count = {}

# Iteracja po słowach
for word in words:
    if word in word_count:
        # Jeśli słowo już jest w słowniku, zwiększ licznik o 1
        word_count[word] += 1
    else:
        # Jeśli słowa nie ma w słowniku, dodaj je z wartością 1
        word_count[word] = 1

# Wyświetlenie wyników
for word, count in word_count.items():
    print(f"The word '{word}' appears {count} times.")
