import time
import sys
import os
sys.path.append('src')
import algo
import util

def main():
    name = input("Nama file input (input1..input5): ")
    filepath = "input/" + name + ".txt"
    if not os.path.isfile(filepath):
        print("File tidak ditemukan.")
        return
    cb = []
    with open(filepath, 'r') as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:
                cb.append(list(clean_line))
    n = len(cb)
    qpos = list(range(n))
    
    count = input("Tampilkan solusi setiap berapa iterasi? (0 untuk tidak menampilkan): ")
    try:
        count = int(count)
    except ValueError:
        print("Input tidak valid. Menggunakan default (0).")
        count = 0
    if count < 0:
        print("Input tidak valid. Menggunakan default (0).")
        count = 0
    if count > 10000:
        print("Input terlalu besar. Menggunakan max (10000).")
        count = 10000
    
    print("Algoritma akan dimulai dalam 3 detik")
    for i in range(3, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)
    print()
    
    start = time.time()
    res, iter = algo.getsolution(cb, qpos, count)
    end = time.time()
    ms = (end- start) * 1000
    lines = None
    
    if res:
        print()
        print("Solusi ditemukan:")
        lines = util.printboard(cb, res)
        print(f"{ms:.2f} ms")
        print(f"Jumlah iterasi: {iter}")
    else:
        lines = None
        print()
        print("Tidak ada solusi.")
        print(f"{ms:.2f} ms")
        print(f"Jumlah iterasi: {iter}")
    print()
    pil = input("Simpan solusi? (y/n): ")
    if pil.lower() != 'y':
        return
    
    os.makedirs("test",exist_ok=True)
    solpath = os.path.join("test", name + "_sol.txt")
    with open(solpath, 'w') as f:
        if lines:
            for line in lines:
                f.write(line + "\n")
        else:
            f.write("Tidak ada solusi.\n")
        f.write(f"{ms:.2f} ms\n")
        f.write(f"Jumlah iterasi: {iter}\n")
    print(f"Solusi disimpan di {solpath}")
        
if __name__ == "__main__":
    main()