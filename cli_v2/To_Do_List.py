# To-do-List-CLI.py 
# V2 - MEnambahkan save & load function .json

import json   # modul python untuk menulis dan membaca file json 
import os     # modul python untuk berinteraksi dengan os ( read, write directory / file)

todo_file = "todolist.json"
1

# membuat tipe data dengan list 
todo_list = [] 

# === Fungsi untuk load dan save data === 
def load_data():
    global todo_list                     # agar bisa mengubah list yang ada diluar fungsi 
    if os.path.exists(todo_file):        # cek file todolist.json sudah ada 
        with open(todo_file, "r") as f:  # membuka file dalam mode read (with digunakan supaya otomatis menutup file suukses / error)
            todo_list = json.load(f)     # baca isi file json dan ubah ke list python biasa 

def save_data():
    with open(todo_file, "w") as f:  # mode write = menimpa isi lama 
        json.dump(todo_list, f)      # ubah list python ke format json dan simpan file 

# === Fungsi menu dan Fitur ===
# tampilkan pilihan ke pengguna 
def show_menu():
    print("\n--- TO DO LIST ---")
    print("1. Tampilkan Daftar")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def tampilkan_daftar():
    if not todo_list:   # cek apakah list kosong 
        print("Belum ada tugas.")
    else:
        # jika ada isinya cetak semua tugas dengan no urut menggunakan enumerate
        # start = 1, untuk memulai no urut dari 1 bukan 0 
        for i, tugas in enumerate(todo_list, start=1):
            print(f"{i}. {tugas}")

def tambah_tugas():
    tugas = input("Masukan Tugas baru: ") # ambil input dari user 
    todo_list.append(tugas)               # menambahkan ke dalam list 
    save_data()
    print(f"Tugas {tugas} ditambahkan")

def hapus_tugas():
    tampilkan_daftar() # menampilkan semua daftar tugas
    try:
        index = int(input("Nomor tugas yang ingin di hapus : "))
        if 1 <= index <= len(todo_list):
            # menghapus index (menggunakan pop(index -1 karena index dimulai dari 0))
            tugas = todo_list.pop(index-1) 
            save_data()
            print(f"Tugas {tugas} dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:                    # menangani error 
        print("Input harus angka.")

# === Main Program === 
load_data()

# looping selama pilihan benar 
while True: 
    show_menu()
    pilihan = input("Pilih menu (1-4).")

    if pilihan == "1":
        tampilkan_daftar()
    elif pilihan == "2":
        tambah_tugas()
    elif pilihan == "3":
        hapus_tugas()
    elif pilihan == "4":
        print("Keluar dari program")
        break
    else:
        print("PIlihan tidak valid")