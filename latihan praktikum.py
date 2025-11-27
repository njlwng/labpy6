# Program Daftar Nilai Mahasiswa (CRUD)

mahasiswa = {}

# ---- FUNGSI TAMBAH DATA ----
def tambah():
    print("\n=== TAMBAH DATA ===")
    nama = input("Nama mahasiswa : ")
    nilai = float(input("Nilai         : "))
    mahasiswa[nama] = nilai
    print("Data berhasil ditambahkan.\n")

# ---- FUNGSI TAMPILKAN DATA ----
def tampilkan():
    print("\n=== DAFTAR NILAI MAHASISWA ===")
    if not mahasiswa:
        print("Belum ada data.\n")
    else:
        for nama, nilai in mahasiswa.items():
            print(f"- {nama} : {nilai}")
        print()

# ---- FUNGSI HAPUS DATA ----
def hapus(nama):
    print("\n=== HAPUS DATA ===")
    if nama in mahasiswa:
        del mahasiswa[nama]
        print(f"Data '{nama}' berhasil dihapus.\n")
    else:
        print("Nama tidak ditemukan.\n")

# ---- FUNGSI UBAH DATA ----
def ubah(nama):
    print("\n=== UBAH DATA ===")
    if nama in mahasiswa:
        nilai_baru = float(input("Nilai baru : "))
        mahasiswa[nama] = nilai_baru
        print(f"Data '{nama}' berhasil diubah.\n")
    else:
        print("Nama tidak ditemukan.\n")

# ---- MENU UTAMA ----
while True:
    print("=== MENU ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama_hapus = input("Nama yang ingin dihapus : ")
        hapus(nama_hapus)
    elif pilihan == "4":
        nama_ubah = input("Nama yang ingin diubah : ")
        ubah(nama_ubah)
    elif pilihan == "5":
        print("\nProgram selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.\n")

