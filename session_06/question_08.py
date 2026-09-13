# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:19:31 2026

@author: Fatemeh
"""

users = [("Ali", 25, "Python"),("Sara", 30, "Java"),("Reza", 22, "Python"),
("Mina", 28, "C++"),("John", 35, "Python"),("David", 30, "Java")
]

a = {}

for name, age, language in users:
    if language in a:
        a[language].append(name)
    else:
        a[language] = [name]

print("گروه‌بندی کاربران:")
print(a)


age_sum = {}
user_count = {}

for name, age, language in users:
    if language in age_sum:
        age_sum[language] += age
        user_count[language] += 1
    else:
        age_sum[language] = age
        user_count[language] = 1

print("میانگین سن:")

for language in age_sum:
    average = age_sum[language] / user_count[language]
    print(language, average)


oldest = {}

for name, age, language in users:
    if language not in oldest:
        oldest[language] = (name, age)
    elif age > oldest[language][1]:
        oldest[language] = (name, age)

print("مسن‌ترین کاربر هر زبان:")
print(oldest)


max_count = 0
best_language = ""

for language, names in a.items():
    count = len(names)

    if count > max_count:
        max_count = count
        best_language = language

print("زبان با بیشترین کاربر:", best_language)
print("تعداد کاربران:", max_count)


languages = list(a.keys())

print("زبان‌های موجود:", languages)