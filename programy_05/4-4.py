
with open('it_company.csv', 'r') as file:
    lines = file.readlines()

total_lines = len(lines)

i = 0


while i < total_lines:

    end = i + 5
    chunk = lines[i:end]
    

    for line in chunk:
        print(line.strip())  
    
    
    input('Press Enter key...')

    

    i = end
