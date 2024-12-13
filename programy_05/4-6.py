def count_file_details(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_chars = sum(len(line) for line in lines)
            num_words = sum(len(line.split()) for line in lines)
        
        return num_lines, num_chars, num_words
    except FileNotFoundError:
        return None, None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None

def main():
    filename = input("Enter the filename: ")
    num_lines, num_chars, num_words = count_file_details(filename)
    
    if num_lines is not None:
        print(f"Number of lines: {num_lines}")
        print(f"Number of characters: {num_chars}")
        print(f"Number of words: {num_words}")
    else:
        print("File not found. Please make sure the filename is correct and try again.")

if __name__ == "__main__":
    main()
