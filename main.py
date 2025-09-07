kwh = int(input("Enter the KW hours used: "))

rate1 = 7.633
rate2 = 9.259

amount = 0

if kwh <= 1000:
    amount = rate1 * kwh

else:
    amount = (rate1 * 1000) + ((kwh - 1000)* rate2)

amount = amount / 100

print("Amount owed: $", amount)


