###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"]
    if n == 1:
        return weekdays[0]
    if n == 2:
        return weekdays[1]
    if n == 3:
        return weekdays[2]
    if n == 4:
        return weekdays[3]
    if n == 5:
        return weekdays[4]
    if n == 6:
        return weekdays[5]
    if n == 7:
        return weekdays[6]
print(weekday(1))
print(weekday(4))
print(weekday(7))
