import csv

def filter_clothing_items(filename):
    try:
        # Open the CSV file
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Use DictReader to automatically use the header row as field names
            # Iterate over each row in the CSV
            for row in reader:
                # Convert price and stock to float and int respectively and check conditions
                if float(row['Price']) < 60 and int(row['Stock_Quantity']) < 40:
                    print(row['Product_Name'], row['Price'], row['Stock_Quantity'])
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# The file path you provide below should be adjusted to the actual path of your file.
filter_clothing_items('clothing.csv')
