#### Implement a program that prompts the user to insert a coin,
### one of a time, each time informing the user of the amount due.
amount_due = 50
coins = [5,10,25]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert Coin: "))

    if coin in coins:
        amount_due -= coin

print(f"Change Owed: {abs(amount_due)}")
#### Once the user has inputted at least 50 cents, output how many cents in chance the user is owed.\

### Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.