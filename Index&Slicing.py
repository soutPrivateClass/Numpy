import numpy as np
from numpy.random import randn,randint
import os

os.system("clear")

# BILANGAN DISTRIBUSI UNIFORM (0 SAMPAI 1) :
angka1 = np.random.rand(7)
print(angka1)

# BILANGAN DISTRIBUSI UNIFORM (0 SAMPAI 1) MATRIX 2 DIMENSI :
angka2 = np.random.rand(4,4)
print(angka2)

# BILANGAN DISTRIBUSI NORMAL (gaussian) ANGKA MULAI DARI (-) TAK HINGGA SAMPAI TAK HINGGA :
angka3 = np.random.randn(10)
print(angka3)

# BILANGAN DISTRIBUSI NORMAL (gaussian) 2 DIMENSI ANGKA MULAI DARI (-) TAK HINGGA SAMPAI TAK HINGGA :;
# CARA NORMAL :

angka4 = angka3 = np.random.randn(4,4)
print(angka4)

# CARA CEPAT :
angka5 = randn(4,4)
print(angka5)

# GENERETE INTEGER :
angka6 = randint(0,10,30) # DARI 0 SAMPAI 10 MENGAAMBIL SEBANYAK 30 ANGKA
print(angka6)

# GENERATE INTEGER 2 DIMENSI MENGGUNAKAN FUNGSI ATAU METHOD RESHAPE :
# HARUS MENGGUNAKANN PECAHAN ANGKA UNUTK MENENTUKAN UKURAN
angka7 = angka6.reshape(5,6) # 5 . 6 = 30, ADALAH BILANGAN YANG SESUAI DENGAN PECAAN
print(angka7)

# CEK ANGKA TRBESAR DARI BILANGAN DIATAS
maximum = angka7.max()
print(maximum)

# CEK ANGKA TERKECIL 
minimum = angka7.min()
print(minimum)

# CEK ANGKA TRBESAR DARI BILANGAN DIATAS DENGAN INDEXING
maximum = angka7.argmax()
print(maximum)

# CEK ANGKA TERKECIL DENGAN INDEXING
minimum = angka7.argmin()
print(minimum)

# CEK SHAPE ATAU MODEL MATRIX
model = angka7.shape
print(model)

# CEK TIPE DATA
dataType = angka7.dtype
print(dataType)

# INDEXING :

angka8 = np.arange(0,10)
print(angka8)

print(angka8[2:8]) # PRINT ANGKA DARI INDEX 2 SAMPAI 8

print(angka8[2:]) # PRINT ANGKA DARI INDEX 2 SAMPAI INDEX TERAKHIR

print(angka8[:10]) # PRINT ANGKA DARI INDEX 0 SAMPAI INDEX TERAKHIR

angka9 = angka8[2:7] # MEMBUAT DATA VARIABEL BARU NAMUN AKAN BERPENGARUH PADA VARIABEL DATA SBELUMNYA YAITU VARIABEL DATA ANGKA 8
angka9[:] = 100

angka9 = angka8.copy() # MEMBUAT DATA VARIABEL BARU NAMUN TIDAK AKAN BERPENGARUH PADA VARIABEL DATA SBELUMNYA YAITU VARIABEL DATA ANGKA 8 MENGGUNAKAN FUNGSI COPY ()
angka9[:] = 200
print(angka9)

# INDEXING 2 PADA DATTA 2 DIMENSI ATAU MATRIX :

angka10 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(angka10)
print(angka10[1,3]) # MENGAMBIL DATA DARI BARIS KE-1 DAN KOLOM KE-3

print(angka10[1:,0:2]) # MENGAMBIL 2 ANGKA DARI MATRIX 2 DIMENSI 

print(50*"=")


angka11 = np.arange(0,11)
angkaBol = angka11 > 4
print(angkaBol)
angkaRand = angka11[angkaBol]
