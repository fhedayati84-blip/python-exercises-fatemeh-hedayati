transactions = [("Ali", "deposit", 5000000),("Ali", "withdraw", 1000000),("Sara", "deposit", 8000000),
 ("Ali", "withdraw", 500000),("Sara", "withdraw", 2000000),("Reza", "deposit", 10000000)
]

def analyze_transactions(transactions):
    result = {}
    for user, transaction_type, value in transactions:
        if user not in result:
            result[user] = {"deposits": 0,"withdrawals": 0,"balance_change": 0,
            "transactions": 0}

        result[user]["transactions"] += 1

        if transaction_type == "deposit":
            result[user]["deposits"] += value
            result[user]["balance_change"] += value
        elif transaction_type == "withdraw":
            result[user]["withdrawals"] += value
            result[user]["balance_change"] -= value

    max_deposit_user = max(result,
        key=lambda user: result[user]["deposits"]
    )

    max_withdrawal_user = max(result,key=lambda user: result[user]["withdrawals"]
    )

    most_active_user = max(result,key=lambda user: result[user]["transactions"]
    )
    return result, max_deposit_user, max_withdrawal_user, most_active_user

result, max_deposit, max_withdrawal, most_active = analyze_transactions(transactions)
print("Analysis:")
for user, data in result.items():
    print(user, data)

print("\nبيشترين واريز:", max_deposit)
print("بيشترين برداشت:", max_withdrawal)
print("فعال ترين کاربر:", most_active)