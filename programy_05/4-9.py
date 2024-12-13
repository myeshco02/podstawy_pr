import csv

def filter_graphic_designers(filename):
    try:
        # Open the CSV file
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Use DictReader to automatically use the header row as field names
            # Iterate over each row in the CSV
            for row in reader:
                # Check if the job title matches 'Graphic Designer'
                if row['Job Title'] == 'Graphic Designer':
                    # Print the required details: first name, last name, and email
                    print(row['First Name'], row['Last Name'], row['Email'])
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the path to the CSV file
filter_graphic_designers('it_company.csv')
