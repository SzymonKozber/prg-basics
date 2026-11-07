def get_month_name(month_num):
    if month_num < 1 or month_num > 12:
        print("Invalid month number. Please enter a number between 1 and 12.")
        return None
    return month_num

# Pobieramy numer od użytkownika i przekazujemy do funkcji
user_input = int(input("Enter month number (1-12): "))
month_num = get_month_name(user_input)

if month_num == 1:
    print("January")
elif month_num == 2:
    print("February")
elif month_num == 3:
    print("March")
elif month_num == 4:
    print("April")
elif month_num == 5:
    print("May")
elif month_num == 6:
    print("June")
elif month_num == 7:
    print("July")
elif month_num == 8:
    print("August")
elif month_num == 9:
    print("September")
elif month_num == 10:
    print("October")
elif month_num == 11:
    print("November")
elif month_num == 12:
    print("December")
