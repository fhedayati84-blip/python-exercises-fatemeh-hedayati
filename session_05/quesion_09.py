username = input("یوزرنیم خود را تعریف کنید: ")
password = input("رمز عبور خود را تعریف کنید: ")

print("\n  (۳ بار فرصت) ")

for eshtebah in range(1, 4):
    print(f"\nتلاش {eshtebah} از ۳:")
    u = input("یوزرنیم: ")
    p = input("رمز عبور: ")

    if u == username and p == password:
        print("\n ورود موفق")
        print("به صفحه خوش آمدی")
        break
    else:
        remaining = 3 - eshtebah
        if remaining > 0:
            print(f" اشتباه، {remaining} بار دیگر فرصت دارید")
        else:
            print(" اشتباه ۳ بار اشتباه کردید،  مسدود شد.")