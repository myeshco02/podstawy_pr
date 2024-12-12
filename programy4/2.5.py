# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

#function counting all seats (no need for argument:3)
def seats_total():
    TotalSeats = 0
    for row in cinema_seats:
        for seat in row:
            TotalSeats+=1
    return TotalSeats

#function counting available seats (same as above)
def seats_available():
    SeatsAv = 0
    for row in cinema_seats:
        for seat in row:
            if seat == "A":
                SeatsAv+=1
    return SeatsAv

#function counting booked seats (boooring)
def seats_booked():
    SeatsBooked = 0
    for row in cinema_seats:
        for seat in row:
            if seat == "B":
                SeatsBooked+=1
    return SeatsBooked

#funtion that compares given position in array, if its A, seat is empty, else its booked
def seat_status(row, place):
    Status=""
    if cinema_seats[row-1][place-1] == "A": #row-1 and place-1 because arrays starts from 0 
        Status = "Available"
    else:
        Status = "Booked"
    return Status

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total())
print('Seats available:',seats_available())
print('Seats booked:', seats_booked())
print('Seat in row 1, place 1:', seat_status(1,1))
print('Seat in row 5, place 5:', seat_status(5,5))
print('Seat in row 3, place 5:', seat_status(3,5))







