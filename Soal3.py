"""
Nama    : Said Muhammad Mazaya
NIM     : 221402129

Soal 3 =  Write a Python program that reads in a number and prints the date 
        that number of days from now in this format: Monday on 25 March 2024.
"""

import datetime

# Input
number = int(input("Enter a number: "))

# Proses
hari_sekarang = datetime.date.today()
result = hari_sekarang + datetime.timedelta(days=number)

# Output
print(f"The date {number} days from now is {result.strftime('%A on %d %B %Y')}")