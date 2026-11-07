###
#Define a function time_string(hours, minutes, time_format) that, given the number of hours (0..23) and the number of minutes (0..59), returns a string specifying the time in the given format ('24' for 24-hour time and '12' for 12-hour time).
#
def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"
    elif time_format == '12':
        period = "AM" if hours < 12 else "PM"
        hours_12 = hours % 12
        hours_12 = 12 if hours_12 == 0 else hours_12
        return f"{hours_12:02}:{minutes:02} {period}"
    else:
        raise ValueError("Invalid time format. Use '24' or '12'.")


print(time_string(15, 38, '24'))
print(time_string(0, 5, '24'))  # returns '00:05'
print(time_string(11, 15, '12'))  # returns '11:15am'
print(time_string(0, 7, '12'))  # returns '12:07am'
print(time_string(7, 30, '12'))  # returns '7:30am'
print(time_string(12, 46, '12'))  # returns '12:46pm'