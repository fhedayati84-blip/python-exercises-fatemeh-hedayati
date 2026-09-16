transactions = [("Ali", "deposit", 50000000, 10),("Ali", "withdraw", 2000000, 11),
    ("Ali", "withdraw", 3000000, 12),("Ali", "withdraw", 4000000, 13),
    ("Ali", "withdraw", 5000000, 14),("Ali", "withdraw", 6000000, 15),
    ("Sara", "deposit", 50000000, 20),("Sara", "withdraw", 60000000, 21),
    ("Reza", "deposit", 150000000, 30)]
def check_transaction(transaction):
    name, trans_type, value, time = transaction
    if value > 100000000:
        return True
    return False
def check_repeated(transactions):
    suspicious = []
    withdraw_count = {}
    for transaction in transactions:
        username, trans_type, value, time = transaction
        if username not in withdraw_count:
            withdraw_count[username] = 0
        if trans_type == "withdraw":
            withdraw_count[username] += 1
            if withdraw_count[username] > 3:
                suspicious.append(transaction)
        else:
            withdraw_count[username] = 0
    return suspicious
def check_balance(transactions):
    suspicious = []
    balance = {}
    for transaction in transactions:
        name, trans_type, value, time = transaction
        if name not in balance:
            balance[name] = 0
        if trans_type == "deposit":
            balance[name] += value
        elif trans_type == "withdraw":
            if value > balance[name]:
                suspicious.append(transaction)
            else:
                balance[name] -= value
    return suspicious
def generate_report(transactions):
    report = []
    repeated_withdrawals = check_repeated(transactions)
    for transaction in transactions:
        if check_transaction(transaction):
            report.append(transaction)
    for transaction in repeated_withdrawals:
        if transaction not in report:
            report.append(transaction)
    balance_frauds = check_balance(transactions)
    for transaction in balance_frauds:
        if transaction not in report:
            report.append(transaction)
    return report
def detect_fraud(transactions):
    return generate_report(transactions)
fraud_report = detect_fraud(transactions)
for transaction in fraud_report:
    print(transaction)