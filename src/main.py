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
    
    start = time.time()
    res, iter = algo.getsolution(cb, qpos)
    end = time.time()
    ms = (end- start) * 1000
    lines = None
    
    if res:
        lines = util.printboard(cb, res)
        print(f"{ms:.2f} ms")
        print(f"Jumlah iterasi: {iter}")
    else:
        lines = None
        print("Tidak ada solusi.")
        print(f"{ms:.2f} ms")
        print(f"Jumlah iterasi: {iter}")
        
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