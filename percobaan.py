import sqlite3

# Membuat koneksi ke database SQLite
def connect_db():
    conn = sqlite3.connect('data_management.db')
    cursor = conn.cursor()
    return conn, cursor

# Membuat tabel jika belum ada
def create_table():
    conn, cursor = connect_db()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        email TEXT)''')
    conn.commit()
    conn.close()

# Menambah data pengguna
def add_user(name, email):
    conn, cursor = connect_db()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    print(f'User {name} has been added.')

# Menampilkan semua data pengguna
def view_users():
    conn, cursor = connect_db()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    if users:
        for user in users:
            print(f'ID: {user[0]}, Name: {user[1]}, Email: {user[2]}')
    else:
        print('No data available.')

# Mengedit data pengguna
def edit_user(user_id, new_name, new_email):
    conn, cursor = connect_db()
    cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (new_name, new_email, user_id))
    conn.commit()
    conn.close()
    print(f'User with ID {user_id} has been updated.')

# Menghapus data pengguna
def delete_user(user_id):
    conn, cursor = connect_db()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    print(f'User with ID {user_id} has been deleted.')

# Menu utama aplikasi
def menu():
    while True:
        print("\n--- Aplikasi Manajemen Data Pengguna ---")
        print("1. Tambah Pengguna")
        print("2. Lihat Pengguna")
        print("3. Edit Pengguna")
        print("4. Hapus Pengguna")
        print("5. Keluar")
        choice = input("Pilih menu (1-5): ")
        
        if choice == '1':
            name = input("Masukkan nama pengguna: ")
            email = input("Masukkan email pengguna: ")
            add_user(name, email)
        
        elif choice == '2':
            view_users()
        
        elif choice == '3':
            user_id = int(input("Masukkan ID pengguna yang ingin diedit: "))
            new_name = input("Masukkan nama baru pengguna: ")
            new_email = input("Masukkan email baru pengguna: ")
            edit_user(user_id, new_name, new_email)
        
        elif choice == '4':
            user_id = int(input("Masukkan ID pengguna yang ingin dihapus: "))
            delete_user(user_id)
        
        elif choice == '5':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Menjalankan aplikasi
if __name__ == "__main__":
    create_table()
    menu()
