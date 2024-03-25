"""
Nama    : Said Muhammad Mazaya
NIM     : 221402129

Soal 1 = Write a Python program that reads in a whole number and divides it by number of days this year and 
    displays the result with eleven decimal places if they exist (rounded up).
"""
import datetime

# Input
number = int(input("Enter a whole number: "))

# Mendapatkan tahun sekarang
current_year = datetime.date.today().year
days_in_year = 366 if datetime.date(current_year, 2, 29).strftime("%j") == '060' else 365

# Proses
result = number / days_in_year
result = round(result, 11)

# Output
print(f"The result of {number} divided by {days_in_year} is {result}")