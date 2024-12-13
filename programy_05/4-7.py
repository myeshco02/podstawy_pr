import re

def count_vowels(text):
    """Count the number of vowels in a given text using regular expressions."""
    # Define the regular expression pattern to find vowels
    pattern = r'[aeiouAEIOU]'
    # Find all matches and return the count
    vowels = re.findall(pattern, text)
    return len(vowels)

def main():
    # Take input from the user
    user_input = input("Enter some text: ")
    # Count vowels in the input text
    vowel_count = count_vowels(user_input)
    # Display the result
    print(f"The text contains {vowel_count} vowels.")

if __name__ == "__main__":
    main()
