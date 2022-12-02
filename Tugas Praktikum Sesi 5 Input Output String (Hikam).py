#!/usr/bin/env python
# coding: utf-8

# <h1>Input</h1>
# 
# Input terdiri dari 2 jenis yaitu
# <ol>
#     <li>Statis (Hardcode)</li>
#     <li>Dinamis</li>
# </ol>
#         
# Input secara statis adalah memberikan nilai kepada variabel secara langsung pada kode program<br>
# Misal:
# ```python
# hari = "Minggu"
# tanggal = 21
# bulan = "Oktober"
# tahun = "2021"
# ```
# Sedangkan input secara dinamis yaitu program menunggu input dari user dimana kursor akan menjadi mode teks dan berkedip-kedip. Input secara dinamis menggunakan fungsi <b>input(s)</b> dimana <b>s</b> adalah string label sebagai keterangan. Berikut ini adalah contoh input dinamis
# ```python
# matakuliah_1 = input('Mata kuliah 1 yang diambil : ')
# matakuliah_2 = input('Mata kuliah 2 yang diambil : ')
# print(f"Anda mengambil mata kuliah  {matakuliah_1} dan {matakuliah_2}")
# ```
# <h3>Latihan</h3>
# <ol>
#     <li>Buatlah variabel dengan nama hobi, yang digunakan untuk menampung input dari user dengan label "Hobi kamu apa? : " , kemudian Cetaklah dengan label <b>Hobi kamu : {hobi}</b></li>
#     <li>Buatlah variabel nama, yang digunakan untuk menampung input dari user dengan label "Siapa nama kamu? : " , misal user mengisikan nama "Romi" maka akan tampil output <b>Nama kamu berawalan huruf R</b></li>
# </ol>

# In[4]:


#Code here
print("==========Hobi==========")
hobi = input('Hobi kamu apa? :')
print(f"Hobi kamu {hobi}")
print("=========Selesai========")


print("=============Variabel nama=============")
nama = input('Siapa nama kamu? :')
print (f"Nama kamu berawalan huruf {nama[0]}")
print("================Selesai================")


# <details>
#     <summary><font color="red">Click Here </font> to See the Answer No.1</summary>
# 
# Jawaban No. 1
#     
# ```python
# hobi = input('Hobi kamu apa? :')
# print(f"Hobi kamu {hobi}")
# ```
# </details>

# <details>
#     <summary><font color="red">Click Here </font> to See the Answer No.2</summary>
# 
# Jawaban No. 2
#     
# ```python
# nama = input('Siapa nama kamu :')
# print(f"Nama kamu berawalan huruf {nama[0]}")
# ```
# </details>

# <h1>Random Bilangan</h1>
# 
# Nilai Random adalah sebuah nilai acak yang dibangkitkan dari pseudocode acak, tapi hal tersebut tidak benar-benar acak. bagaimana mungkin mendapatkan nilai acak, jika masih menggunakan alur program. Random pada python dapat menghasilkan nilai berupa integer, float maupun string.
# Untuk membuat Random value maka dapat menggunakan fungsi <b>random</b>. Sebelum fungsi <b>random</b> digunakan, maka terlebih dahulu harus melakukan import library. Perhatikan contoh berikut ini:
# 
# <h3>Random Float</h3>
# 
# ```python
# # mengimport library random
# from random import random
# # mengacak bilangan float
# nilai = random()
# # mencetak bilangan random
# print(nilai)
# ```
# 
# <h3>Random Integer</h3>
# 
# ```python
# # mengimport library random
# from random import randint
# # mengacak bilangan integer dengan range 0-10
# nilai = randint(0,10)
# # mencetak bilangan random
# print(nilai)
# ```
# <h3>Random Choice</h3>
# 
# ```python
# from random import choice
#  
# # list of month
# bulan = ["Jan", "Feb", "Mar", "Apr", "May","Jun","Jul","Aug","Sep","Oct","Nov","Des"]
#  
# # memilih dari list scr acak
# pilih_bulan = choice(bulan)
# print(pilih_bulan)
# ```
# 
# <h3>Latihan</h3>
# 
# <ol>
#     <li>Buatlah program tebak hasil dari perkalian dari 2 angka dari 0 sampai 100, jika user menjawab benar maka tampil <b>Jawaban anda True</b> dan jika salah, maka akan tampil <b>Jawaban anda False</b></li>
# </ol>

# In[2]:


#Code Here
from random import randint

nilai1 = randint(0,100)
nilai2 = randint(0,100)
hasil = nilai1 * nilai2

jawab = int(input("Berapa hasil perkalian dari {} dan {} ? = ".format(nilai1,nilai2)))
print("Jawaban anda {}".format(jawab==hasil))


# <details>
#     <summary><font color="red">Click Here </font> to See the Answer No.1</summary>
# 
# Jawaban Tebak Perkalian 2 Angka
#     
# ```python
# from random import randint
# angka_1 = randint(0,100)
# angka_2 = randint(0,100)
# 
# hasil = int(input(f"Berapakah hasil perkalian {angka_1} dan {angka_2} : "))
# print(f"Jawaban anda {hasil==angka_1 * angka_2}")
# ```
# </details>

# 
# <h1>Output</h1>
# 
# Output adalah sebuah hasil keluaran dari sebuah program. Output terdiri dari ada 2 jenis yaitu:
# <ol>
#     <li>Output yang ditampilkan di layar (CLI)</li>
# 	<li>Output yang (ditulis) dalam bentuk file</li>
# </ol>
# Pada kesempatan kali ini, kita hanya akan membahas jenis output yang pertama yaitu output yang ditampilkan di layar (secara CLI), sehingga pembahasannya akan lebih banyak mengenai variasi cara menggunakan fungsi print() pada python.
# 
# <h3>Fungsi print()</h3>
# 
# Fungsi dasar print()
# ```python
# print('Selamat kuliah')
# ```
# Fungsi print multi argument
# ```python
# print('Budi','Roni','Andri')
# ```
# Fungsi print fstring
# ```python
# nama = 'Lita'
# print(f"Selamat datang {nama}")
# ```
# Fungsi print dengan tanda pemisah
# ```python
# print('andi','tedi','fahmi',sep='\U0001F600')
# print("\N{smiling face with halo}")
# ```
# Fungsi print dengan format
# ```python
# a=10
# b=15
# c=20
# print('{} + {} + {} adalah {}'.format(a,b,c,a+b+c))
# ```
# Fungsi print dengan index
# ```python
# print('{} dan {}'.format('Roni','Huda'))
# print('{1} dan {0}'.format('Roni','Huda'))
# ```
# 
# <h3>Latihan</h3>
# Carilah kode CLDR Names dan unicode dari emoji, dan cetaklah menggunakan fungsi print

# In[2]:


#Code here
print("Emoji Yang Muncul :\N{grinning face}")
print("Emoji Yang Muncul :\N{slightly smiling face}")
print("Emoji Yang Muncul :\N{winking face}")
print("Emoji Yang Muncul :\N{zipper-mouth face}")
print("Emoji Yang Muncul :\N{rolling on the floor laughing}")


# <h1>String</h1>
# String adalah kumpulan dari beberapa karakter. String dibuat dengan tanda petik tunggal (') atau ganda (")
# Contoh:
# 
# ```python
# kota ='Surabaya'
# provinsi ='Jawa Timur'
# ```
# Karena string tersusun dari kumpulan karakter, maka string dapat diambil per karakternya menggunakan index yang diapit oleh kurung siku [] atau dengan range [indeks-awal:indeks-akhir]
# Contoh:
# ```python
# kalimat = 'Apa kabar semua hari ini?'
# print(kalimat[0]) #A
# print(kalimat[1]) #p
# print(kalimat[0:3]) #Apa
# print(kalimat[4:9]) #kabar
# print(kalimat[:-10]) #Apa kabar semua
# print(kalimat[-9:]) #hari ini?
# print(kalimat[-15:-5]) #semua hari
# ```
# <h3>Latihan</h3>
# Jika terdapat sebuah string <b>Belajar Pemrograman Python</b> Maka tampilkan <b>output</b> berikut ini menggunakan fungsi <b>print</b><br>
# <ol>
#     <li>Belajar</li>
#     <li>ajar</li>
#     <li>Pemrograman</li>
#     <li>gram</li>
#     <li>Python</li>
#     <li>Py</li>
#     <li>gram Python</li>
#     <li>Pemrograman Python</li>
# </ol>
# 

# In[35]:


#Code here
kata = "Belajar ajar Pemrograman gram Python Py gram Python Pemrograman Python"
print("1.Kata Yang Keluar Adalah:",kata[0:7])
print("2.Kata Yang Keluar Adalah:",kata[8:12])
print("3.Kata Yang Keluar Adalah:",kata[13:25])
print("4.Kata Yang Keluar Adalah:",kata[25:29])
print("5.Kata Yang Keluar Adalah:",kata[30:36])
print("6.Kata Yang Keluar Adalah:",kata[37:39])
print("7.Kata Yang Keluar Adalah:",kata[40:51])
print("8.Kata Yang Keluar Adalah:",kata[-18:])


# <h1>String Method</h1>
# String mempunyai banyak method yang dapat digunakan untuk mempercepat menyelesaikan permasalahan, diantaranya adalah:
# <h3>Upper</h3>
# Fungsi upper digunakan untuk mengubah string menjadi huruf kapital. Fungsi tersebut tidak memerlukan parameter/argumen 
# 
# ```python
# kalimat = 'Belajar python sangat Mudah'
# kapital = kalimat.upper()
# print(kapital)
# ```
# Jika program tersebut dijalankan akan menghasilkan output <b>BELAJAR PYTHON SANGAT MUDAH</b>
# 
# <h3>Lower</h3>
# Fungsi lower digunakan untuk mengubah string menjadi huruf kecil. Fungsi tersebut tidak memerlukan parameter/argumen 
# 
# ```python
# kalimat = 'Belajar python sangat Mudah'
# lcase = kalimat.lower()
# print(lcase)
# ```
# Jika program tersebut dijalankan akan menghasilkan output <b>belajar python sangat mudah</b>
# 
# <h3>Find</h3>
# Fungsi find digunakan untuk mencari string untuk nilai tertentu dan mengembalikan posisi ditemukan 
# 
# ```python
# kalimat = 'Belajar python sangat Mudah'
# cari_huruf_p = kalimat.find('p')
# print(cari_huruf_p)
# ```
# Jika program tersebut dijalankan akan menghasilkan output <b>8</b> artinya huruf p ada di urutan ke 8. Perlu diingat bahwa posisi indeks dimulai dari angka 0
# 
# <h1>Latihan</h1>
# 1. Buatlah program untuk mengecek bahwa sebuah email termasuk valid atau tidak. Valid diartikan <b>True</b> dan tidak valid diartikan <b>False</b>
# Berikut contoh <i>test case</i> yang bisa digunakan sebagai acuan 
# <ol>
#     <li>alunsujjada@gmailcom -> False</li>
#     <li>alunsujjada@gmail.com -> True</li>
#     <li>alun.sujjada@gmail.com -> False</li>
#     <li>alunsujjada.gmail.com -> False</li>
#     <li>alun.sujjada@gmailcom -> False</li>
# </ol>

# In[5]:


#Code here
print("=====Menentukan Nilai True Atau False=====")
email = input('Masukan Email : ')
valid_email = '@gmail.com'
if valid_email in email:
    print(email, ' -> ', True)
else:
    print(email, ' -> ', False)

