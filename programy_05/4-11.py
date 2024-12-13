def calculate_powers():
    # Open a text file to write the results
    with open('powers.txt', 'w') as file:
        # Iterate over integers from 1 to 100
        for i in range(1, 101):
            # Calculate second power (i^2) and third power (i^3)
            second_power = i ** 2
            third_power = i ** 3
            # Create a formatted string for the current integer and its powers
            line = f"{i},{second_power},{third_power}\n"
            # Print the line
            print(line.strip())
            # Write the line to the file
            file.write(line)

# Run the function
calculate_powers()
