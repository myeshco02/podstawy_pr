###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
x = 0

# Count vowels in the text
while x < len(text): # loop continues for as long as there is characteres in the text
    if text[x] in vowels: # checking if current character (x in text) is a vowel
        vowel_count += 1 # if it's a vowel, then increase by 1
    x += 1 # move to next character
print(f"The number of vowels in the text is: {vowel_count}")
