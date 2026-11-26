

# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

# Calculates expenses
food_total = 0
transport_total = 0
utilities_total = 0

weekly_totals = []
total_monthly = 0

for row in monthly_expenses:
    # Sumowanie kategorii (kolumn)
    food_total += row[0]
    transport_total += row[1]
    utilities_total += row[2]
    
    # Sumowanie pojedynczego tygodnia (wiersza)
    week_sum = 0
    for item in row:
        week_sum += item
        total_monthly += item
    weekly_totals.append(week_sum)

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', weekly_totals[0])
print('Week 2:', weekly_totals[1])
print('Week 3:', weekly_totals[2])
print('Week 4:', weekly_totals[3])
print('---------------')
print('TOTAL:', total_monthly)