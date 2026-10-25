
###
# Write a program that checks whether the EAN-13 number entered from 
# the keyboard consists of exactly 13 characters
#

ean_13 = input("Enter EAN-13 article number: ")
if len(ean_13) == 13:
  print("Article number is correct")

  if ean_13[:3] == "590":
    print("Article manufactured in Poland")
else:
  print("Article number is incorrect")