def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('pets.txt')
file_lines = file_content.splitlines()

line_number = 1

for line in file_lines:
    word_count = len(line.split())
    print(f"{line} --> {word_count} words")
    line_number += 1