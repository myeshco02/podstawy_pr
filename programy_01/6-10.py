###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('TITLE: ', movie.upper())

# print title in small letters
print('title: ', movie.casefold())

# print how many times the vowel "e" appears in the title
print('Number of "e": ', movie.count('e'))

# print where in the text is the word "Lord"
print('Where "Lord": ', movie.rfind('Lord'))

# print where in the text is the word "dragon"
print('Where "dragon": ', movie.rfind('dragon'))
