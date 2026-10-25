###
# Converts time in 24-hour format to 12-hour format.
#
time_24 = input('Enter time (24-hour format): ')

# Rozdzielenie na godziny i minuty
hours = int(time_24.split(':')[0])
minutes = time_24.split(':')[1]

# Określenie am/pm i przeliczenie godziny
if hours >= 12:
    period = 'pm'
    if hours > 12:
        hours = hours - 12
else:
    period = 'am'
    if hours == 0:
        hours = 12

# Wyświetlenie wyniku
print(f'Time in 12-hour format: {hours}:{minutes}{period}')