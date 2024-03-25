"""
Nama    : Said Muhammad Mazaya
NIM     : 221402129

Soal 5 =  Write a program that reads in integer numbers from a text file named input.txt in 
        the same directory as the executing program.
        Print the sum of the numbers with comma separators and three digits.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

with open(file_path, 'r') as file:
    data = file.readlines()
    
data = [int(x) for x in data] 

sum_data = sum(data)

print(f'{sum_data:,.3f}')


