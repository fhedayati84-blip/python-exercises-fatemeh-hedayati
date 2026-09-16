logs = [("Ali", "LOGIN", 200),("Ali", "DOWNLOAD", 200),("Sara", "LOGIN", 403),
    ("Reza", "LOGIN", 200),("Sara", "LOGIN", 403),("Sara", "LOGIN", 403),]
def detect(logs_list):
    successful_logins = 0
    unsuccessful_logins = 0
    counts = {}
    user_operations = {}
    for user, action, status in logs_list:
        if user not in user_operations:
            user_operations[user] = 1
        else:
            user_operations[user] += 1
        if action == "LOGIN":
            if status == 200:
                successful_logins += 1
            else:
                unsuccessful_logins += 1
        if status == 403:
            if user not in counts:
                counts[user] = 1
            else:
                counts[user] += 1
    suspicious_users = []
    for user, count in counts.items():
        if count >= 3:
            suspicious_users.append(user)
    print(" گزارش نهایی ")
    print(f" تعداد Login موفق: {successful_logins}")
    print(f" تعداد Login ناموفق: {unsuccessful_logins}")    
    if suspicious_users:
        print(f" کاربران مشکوک : {', '.join(suspicious_users)}")
    else:
        print(" هیچ کاربر مشکوکی یافت نشد.")
        
    print(" تعداد کل عملیات هر کاربر:")
    for user, count in user_operations.items():
        print(f"   - {user}: {count} عملیات")
detect(logs)