# Purwadhika JCDS Coding Challenge

Pada repo ini, saya akan menjelaskan tentang coding challenge project yang diadakan di kampus tempat saya belajar, yaitu Purwadhika Startup & Coding School.

Pada coding challenge kali ini, kami diminta untuk berkelompok 5-5. Lalu salah satu laptop dari tiap kelompok harus ditempatkan di depan ruangan. Laptop tersebut nantinya akan dipakai mengoding bergantian. Tiap member kelompok punya waktu 2 menit untuk coding, sebelum bergantian dengan member yang lain.

Kelompok saya ada:
1. Mas Bintang
2. Mas Sholeh Anshori
3. Mas Kelvin Leo
4. Mba Linda

Soal yang harus kita kerjakan adalah:

![alt text](https://github.com/ridhoaryo/jcds_coding_clhallenge/blob/master/soal.jpg "Soal")

Yang menarik dari soal ini adalah, beberapa hari sebelumnya kita pernah diberi soal yang hampir mirip, yaitu mengubah posisi list dalam list (matrix)

```
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

diubah menjadi,

[
    [7,4,1],
    [8,5,2],
    [9,6,3]
]
```
Jujur, saya ngga nemu logic nya hahaha.
Semua kelompok, termasuk kelompok saya. Berpikir bahwa soal di atas adalah tentang matrix, seperti soal beberapa hari lalu. Tapi entah dari mana saya berpikir, ini bukan tentang matrix. Ini cuma permainan for loops dan tambah-kurang saja. Lalu kita tulis di tiap sheet.

## Let's breakdown the code
```
import xlsxwriter

file = xlsxwriter.Workbook('file.xlsx')
sheet1 = file.add_worksheet('sheet 1')
sheet2 = file.add_worksheet('sheet 2')
sheet3 = file.add_worksheet('sheet 3')
sheet4 = file.add_worksheet('sheet 4')
```
Pertama-tama, import xlsxwriter. Buat variable untuk membuat file `file.xlsx`. Buat sheet1, sheet2, sheet3, sheet4 untuk menulis data di tiap sheet.

```
n = 1
for r in range(3):
    for c in range(3):
        sheet1.write(r,c,n)
        n +=1

n2 = 1
for r in range(3):
    for c in range(3):
        sheet2.write(r,c,n2)
        n2 +=3
    n2 -= 8

n3 = 3
for r in range(3):
    for c in range(3):
        sheet3.write(r,c,n3)
        n3 -=1
    n3+=6

n4 = 9
for r in range(3):
    for c in range(3):
        sheet4.write(r,c,n4)
        n4 -=3
    n4+=8
```
Coba dipahami codingnya. Kita di sini cuma mendeklarasi nilai awal di tiap sheet (0,0 atau A1) lalu kita iterasi dengan double `for loops` untuk row dan kolomnya. Lalu tulis di tiap sheet pada row tertentu, kolom tertentu, print angkanya. Sudah. Hasilnya bisa dilihat di `file.xlsx`.

Sekian yang bisa sharing, terimakasih.
