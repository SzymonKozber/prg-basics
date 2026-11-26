# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = 0
   for row in seats:
      total += len(row)
   return total

def seats_available(seats):
   total_available = 0
   for row in seats:
      for char in row:
         if char == "A":
            total_available += 1
   return total_available

def seats_booked(seats):
   total_booked = 0
   for row in seats:
      for char in row:
         if char == "B":
            total_booked += 1
   return total_booked

def seat_status(seats, row, place):
   if seats[row - 1][place - 1] == 'A':
      return 'available'
   else:
      return 'booked'

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))