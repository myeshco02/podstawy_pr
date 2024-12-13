import re

def filter_filenames_with_four_char_extensions():
    # Open and read the file containing the filenames
    try:
        with open('files.txt', 'r', encoding='utf-8') as file:
            filenames = file.readlines()
    except FileNotFoundError:
        print("The file 'files.txt' could not be found.")
        return

    # Define a regular expression to match file extensions with exactly four characters
    pattern = r'\.\w{4}\b'

    # Filter and print filenames matching the pattern
    for filename in filenames:
        filename = filename.strip()  # Remove any leading/trailing whitespace
        if re.search(pattern, filename):
            print(filename)

def main():
    filter_filenames_with_four_char_extensions()

if __name__ == "__main__":
    main()
