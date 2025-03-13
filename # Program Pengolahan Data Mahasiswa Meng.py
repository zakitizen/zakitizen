# Program Pengolahan Data Mahasiswa Menggunakan Array Biasa

# Kamus array untuk menyimpan data mahasiswa
NIM = []
Nama = []
NilaiAkhir = []
IndeksNilai = []

# Fungsi untuk menghitung indeks nilai berdasarkan nilai akhir
# I.S. Nilai terdefinisi
# F.S. Mengembalikan indeks nilai berupa karakter (A, B, C, atau D)
def hitung_indeks_nilai(nilai):
    if 80 <= nilai <= 90:
        return 'A'
    elif 70 <= nilai < 80:
        return 'B'
    elif 60 <= nilai < 70:
        return 'C'
    elif 0 <= nilai < 60:
        return 'D'
    else:
        return '-'

# Prosedur untuk menampilkan data mahasiswa
# I.S. List NIM, Nama, NilaiAkhir, dan IndeksNilai terdefinisi
# F.S. Data mahasiswa ditampilkan ke layar dalam bentuk tabel
def tampilkan_data():
    print(f"{'No':<5}{'NIM':<15}{'Nama':<20}{'Nilai Akhir':<15}{'Indeks':<10}")
    print("-" * 60)
    for i in range(len(NIM)):
        print(f"{i + 1:<5}{NIM[i]:<15}{Nama[i]:<20}{NilaiAkhir[i]:<15.2f}{IndeksNilai[i]:<10}")

# Prosedur untuk mengurutkan data secara ascending berdasarkan nilai akhir
# I.S. List NIM, Nama, NilaiAkhir, dan IndeksNilai terdefinisi
# F.S. List diurutkan secara ascending berdasarkan NilaiAkhir (by reference)
def bubble_sort_ascending():
    n = len(NIM)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if NilaiAkhir[j] > NilaiAkhir[j + 1]:
                # Tukar Nilai Akhir
                NilaiAkhir[j], NilaiAkhir[j + 1] = NilaiAkhir[j + 1], NilaiAkhir[j]
                # Tukar NIM
                NIM[j], NIM[j + 1] = NIM[j + 1], NIM[j]
                # Tukar Nama
                Nama[j], Nama[j + 1] = Nama[j + 1], Nama[j]
                # Tukar Indeks Nilai
                IndeksNilai[j], IndeksNilai[j + 1] = IndeksNilai[j + 1], IndeksNilai[j]

# Prosedur untuk mengurutkan data secara descending berdasarkan nama
# I.S. List NIM, Nama, NilaiAkhir, dan IndeksNilai terdefinisi
# F.S. List diurutkan secara descending berdasarkan Nama (by reference)
def bubble_sort_descending():
    n = len(NIM)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if Nama[j] < Nama[j + 1]:
                # Tukar Nama
                Nama[j], Nama[j + 1] = Nama[j + 1], Nama[j]
                # Tukar NIM
                NIM[j], NIM[j + 1] = NIM[j + 1], NIM[j]
                # Tukar Nilai Akhir
                NilaiAkhir[j], NilaiAkhir[j + 1] = NilaiAkhir[j + 1], NilaiAkhir[j]
                # Tukar Indeks Nilai
                IndeksNilai[j], IndeksNilai[j + 1] = IndeksNilai[j + 1], IndeksNilai[j]

# Prosedur untuk menampilkan menu pengurutan dan melakukan pengurutan
# I.S. List NIM, Nama, NilaiAkhir, dan IndeksNilai terdefinisi
# F.S. Data mahasiswa diurutkan dan ditampilkan sesuai pilihan pengguna
def menu_pengurutan():
    print("Pilih jenis pengurutan:")
    print("1. Urutkan berdasarkan NIM (Ascending)")
    print("2. Urutkan berdasarkan Nama (Descending)")
    print("3. Urutkan berdasarkan Nilai Akhir (Ascending)")
    print("4. Tampilkan data tanpa pengurutan")
    pilihan = int(input("Masukkan pilihan (1/2/3/4): "))

    if pilihan == 1:
        bubble_sort_ascending()
        print("Data setelah diurutkan berdasarkan NIM (Ascending):")
        tampilkan_data()
    elif pilihan == 2:
        bubble_sort_descending()
        print("Data setelah diurutkan berdasarkan Nama (Descending):")
        tampilkan_data()
    elif pilihan == 3:
        bubble_sort_ascending()
        print("Data setelah diurutkan berdasarkan Nilai Akhir (Ascending):")
        tampilkan_data()
    elif pilihan == 4:
        print("Data tanpa pengurutan:")
        tampilkan_data()
    else:
        print("Pilihan tidak valid.")

# Prosedur untuk memasukkan data mahasiswa
# I.S. List NIM, Nama, NilaiAkhir, dan IndeksNilai belum terdefinisi
# F.S. List NIM, Nama, NilaiAkhir, dan IndeksNilai terisi dengan data mahasiswa
def input_data():
    print("Masukkan data mahasiswa:")
    while True:
        nim = input("Masukkan NIM (ketik 'STOP' untuk berhenti): ")
        if nim == "STOP":
            break
        nama = input("Masukkan Nama Mahasiswa: ")
        nilai_akhir = float(input("Masukkan Nilai Akhir: "))
        indeks = hitung_indeks_nilai(nilai_akhir)

        # Simpan data ke dalam list
        NIM.append(nim)
        Nama.append(nama)
        NilaiAkhir.append(nilai_akhir)
        IndeksNilai.append(indeks)

# Program utama
print("Program Pengolahan Data Mahasiswa")
input_data()
menu_pengurutan()