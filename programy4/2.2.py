tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

# Loop through each row in the board
for row in tic_tac_toe_board:
    # Loop through each element in the row
    for cell in row:
        print(cell, end=" ")  # Print each cell with a space, staying on the same line
    print()  # Move to the next line after printing the row
