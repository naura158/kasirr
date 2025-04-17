#daftar untuk menambah siswa 
siswa_list = []

#penambahan siswa 
def add_siswa(nama, nis, jurusan, nilai):
    siswa_list.append({"nama": nama, "nis": nis, "jurusan": jurusan, "nilai": nilai})
    print(f'siswa {nama} telah ditambahkan.')

# menampilkan siswa
def view_siswa():
    if siswa_list:
        for i, siswa in enumerate(siswa_list, 1):
            print(f'ID: {i}, Nama: {siswa["nama"]}, NIS: {siswa["nis"]}, Jurusan: {siswa["jurusan"]}, Nilai: {siswa["nilai"]}')
        else:
            print('Tidak ada data siswa.')

 