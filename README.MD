# Nama : Muhammad Adam Mirza
# NIM : 18223015

## Deskripsi
Program mencari penempatan satu queen (`#`) per baris sedemikian rupa sehingga:
- Setiap queen menempati region yang berbeda.
- Tidak ada dua queen yang bersebelahan secara vertikal (selisih kolom ≤ 1 antar baris berturut-turut).

Solusi dicari menggunakan algoritma **brute force** dengan pendekatan permutasi.

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