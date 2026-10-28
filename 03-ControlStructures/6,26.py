
pin = "2805"
attempts = 0

while attempts < 3:
    entered_pin = input("Enter the pin: ")
    
    if entered_pin == pin:
        print("Approved")
        break  # Poprawny PIN - wychodzimy z pętli
    else:
        attempts += 1
        print("Incorrect")

# Jeśli pętla zakończy się po 3 nieudanych próbach:
if attempts == 3:
    print("Sorry your payment card has been blocked.")