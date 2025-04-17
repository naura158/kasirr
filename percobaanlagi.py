import sqlite3

# Membuat koneksi ke database SQLite
def connect_db():
    conn = sqlite3.connect('manajemen_data_siswa.db')
    cursor = conn.cursor()
    return conn, cursor

# Membuat tabel siswa jika belum ada
def create_table():
    conn, cursor = connect_db()
    cursor.execute('''CREATE TABLE IF NOT EXISTS siswa (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama TEXT,
                        nis TEXT,
                        jurusan TEXT)''')
    conn.commit()
    conn.close()

# Menambah data siswa
def add_siswa(nama, nis, jurusan):
    conn, cursor = connect_db()
    cursor.execute('INSERT INTO siswa (nama, nis, jurusan) VALUES (?, ?, ?)', (nama, nis, jurusan))
    conn.commit()
    conn.close()
    print(f'Siswa {nama} dengan NIS {nis} telah ditambahkan.')

# Menampilkan semua data siswa
def view_siswa():
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM siswa')
    siswa_list = cursor.fetchall()
    conn.close()
    if siswa_list:
        for siswa in siswa_list:
            print(f'ID: {siswa[0]}, Nama: {siswa[1]}, NIS: {siswa[2]}, Jurusan: {siswa[3]}')
    else:
        print('Data siswa kosong.')

# Mengedit data siswa
def edit_siswa(id_siswa, nama_baru, nis_baru, jurusan_baru):
    conn, cursor = connect_db()
    cursor.execute('UPDATE siswa SET nama = ?, nis = ?, jurusan = ? WHERE id = ?', 
                   (nama_baru, nis_baru, jurusan_baru, id_siswa))
    conn.commit()
    conn.close()
    print(f'Data siswa dengan ID {id_siswa} telah diperbarui.')

# Menghapus data siswa
def delete_siswa(id_siswa):
    conn, cursor = connect_db()
    cursor.execute('DELETE FROM siswa WHERE id = ?', (id_siswa,))
    conn.commit()
    conn.close()
    print(f'Siswa dengan ID {id_siswa} telah dihapus.')

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
    create_table()
    menu()
