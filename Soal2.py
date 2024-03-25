"""
Nama    : Said Muhammad Mazaya
NIM     : 221402129

Soal 2 =  Write a Python program that reads a number (today's test date) and prints 
        the product of all the values from 1 to that number.
"""
number = int(input("Masukkan tanggal hari ini : "))

product = 1  
num_string = "1"  

for i in range(1, number + 1):
    product *= i
    num_string += f" * {i}"

print(f"Hasil Perkalian dari 1 sampai {number} adalah {num_string} : {product}")