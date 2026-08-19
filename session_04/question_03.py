"""ramz vard konid 4 karakter aval horof 4 ta dovom adad bashad agar ramz 
dorost bod معتبرast agar nadorst bod معتبر ast"""


ramz=input("رمز عبور وارد کنید:")
if len(ramz) == 8 and ramz [:4].isalpha() and ramz[4:].isdigit():
    print("معتبر")
else:
    print("نامعتبر")