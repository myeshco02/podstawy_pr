import random

dice_roll = random.randint(1, 6)
special = dice_roll in (1, 6)

print(f"""Dice roll: {dice_roll}
Special number (1 or 6): {special}""")