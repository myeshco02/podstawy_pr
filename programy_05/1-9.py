###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

with open("it_company.csv", 'r') as file:
   file_content = file.read()
   file_lines = file_content.splitlines()

for line in file_lines:
    if job_title in line:
        print(line)