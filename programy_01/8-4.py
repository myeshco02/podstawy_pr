###
# A program that prints your height both in cm and in feet and inches.
#
cm = 199
feet = 199 // 30.48
inches = 199 % 30.48
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches: ,.0f} inches')