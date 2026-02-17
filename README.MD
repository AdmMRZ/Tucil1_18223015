# Nama : Muhammad Adam Mirza
# NIM : 18223015

## Deskripsi
Program ini menyelesaikan permainan Queens menggunakan algoritma Brute Force. 
Tujuannya mencari posisi 1 Queen per baris, kolom, dan region warna, dengan syarat tidak ada dua Queen yang saling bersentuhan (baik tegak lurus maupun diagonal).

## Requirement
- Python 3.x

## Cara Menjalankan

### Melalui terminal
```sh
cd src
python main.py
```

### Melalui run.bat
```sh
cd bin
run.bat
```

Program akan meminta input nama file (contoh: `input1` s.d. `input5`). File input harus berada di folder `input/`.

Hasil solusi akan ditampilkan di console dan disimpan di folder `test/` dengan format `inputX_sol.txt`.

## Struktur Folder
```
bin/        -> script untuk menjalankan program
doc/        -> laporan
input/      -> file input board
src/        -> source code program
test/       -> output solusi
```