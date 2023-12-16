import numpy as np
import os

os.system("clear")

"""
OPERASI PADA NUMPY DILAKUKAN PADA SETIAP BILANGAN DALAM LIST ARRAY
"""

angka1 = np.arange(0,11)
print(angka1)

# PENJUMLAHAN
penjumlaan = angka1 + 2
print(penjumlaan)

# PERKALIAN
perkalian = angka1 * 2
print(perkalian)

# PEMBAGIAN
pembagian = angka1 / 2
print(pembagian)

# AKAR 
akar = np.sqrt(angka1) # MENGGUNAKAN METHOD sqrt 
print(akar)

# EXPONENSIAL / EXPONEN / PANGKAT E
exponen = np.exp(angka1)
print(exponen)

"""
MASIH BANYAK LAGI DI DOKUMENTASI NUMPY PADA WEBSITE GOODLUCK !!!
"""

