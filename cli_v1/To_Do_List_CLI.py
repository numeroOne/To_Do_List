# To-do-List-CLI.py 
# membuat tipe data dengan list 
# kenapa list karena bisa menambah dan menghapus item 
todo_list = [] 

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
    todo_list.append(tugas)  # menambahkan ke dalam list 
    print(f"Tugas {tugas} ditambahkan")

def hapus_tugas():
    tampilkan_daftar() # menampilkan semua daftar tugas
    try:
        index = int(input("Nomor tugas yang ingin di hapus : "))
        if 1 <= index <= len(todo_list):
            # menghapus index (menggunakan pop(index -1 karena index dimulai dari 0))
            tugas = todo_list.pop(index-1) 
            print(f"Tugas {tugas} dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:  # menangani error 
        print("Input harus angka.")

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