###
# A program that checks whether the influencer is good that is whether the person 
# has at least two of the following accounts
#
facebook = True
twitter = False
instagram = True

print(f"facebook = {facebook}")
print(f"twitter = {twitter}")
print(f"instagram = {instagram}")

if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):
  print("You are a good influencer!")
else:
  print("You are not a good influencer.")