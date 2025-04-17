# Daftar untuk menyimpan data siswa
siswa_list = []

# Fungsi untuk menambah siswa
def add_siswa(nama, nis, jurusan):
    siswa_list.append({"nama": nama, "nis": nis, "jurusan": jurusan})
    print(f'Siswa {nama} telah ditambahkan.')

# Fungsi untuk menampilkan semua siswa
def view_siswa():
    if siswa_list:
        for i, siswa in enumerate(siswa_list, 1):
            print(f'ID: {i}, Nama: {siswa["nama"]}, NIS: {siswa["nis"]}, Jurusan: {siswa["jurusan"]}')
    else:
        print('Tidak ada data siswa.')

# Fungsi untuk mengedit data siswa
def edit_siswa(id_siswa, nama_baru, nis_baru, jurusan_baru):
    if 0 < id_siswa <= len(siswa_list):
        siswa_list[id_siswa - 1] = {"nama": nama_baru, "nis": nis_baru, "jurusan": jurusan_baru}
        print(f'Siswa dengan ID {id_siswa} telah diperbarui.')
    else:
        print('ID siswa tidak valid.')

# Fungsi untuk menghapus data siswa
def delete_siswa(id_siswa):
    if 0 < id_siswa <= len(siswa_list):
        siswa_list.pop(id_siswa - 1)
        print(f'Siswa dengan ID {id_siswa} telah dihapus.')
    else:
        print('ID siswa tidak valid.')

# Menu utama aplikasi
def menu():
    while True:
        print("\n--- Aplikasi Manajemen Data Siswa ---")
        print("1. Tambah Siswa")
        print("2. Lihat Siswa")
        print("3. Edit Siswa")
        print("4. Hapus Siswa")
        print("5. Keluar")
        choice = input("Pilih menu (1-5): ")
        
        if choice == '1':
            nama = input("Masukkan nama siswa: ")
            nis = input("Masukkan NIS siswa: ")
            jurusan = input("Masukkan jurusan siswa: ")
            add_siswa(nama, nis, jurusan)
        
        elif choice == '2':
            view_siswa()
        
        elif choice == '3':
            id_siswa = int(input("Masukkan ID siswa yang ingin diedit: "))
            nama_baru = input("Masukkan nama baru siswa: ")
            nis_baru = input("Masukkan NIS baru siswa: ")
            jurusan_baru = input("Masukkan jurusan baru siswa: ")
            edit_siswa(id_siswa, nama_baru, nis_baru, jurusan_baru)
        
        elif choice == '4':
            id_siswa = int(input("Masukkan ID siswa yang ingin dihapus: "))
            delete_siswa(id_siswa)
        
        elif choice == '5':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Menjalankan aplikasi
if __name__ == "__main__":
    menu()
