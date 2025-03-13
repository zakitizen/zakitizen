# Program Pengolahan Data Transaksi Laundry
# I.S.: Pengguna memasukkan kode transaksi (KodeTrk), nama pelanggan (Nama), jenis layanan (JenisLayanan), dan berat cucian (Berat)
# F.S.: Menampilkan daftar transaksi laundry dengan fitur sorting, searching, penambahan data, dan penghapusan data

import os

# Konstanta
MAKS_TRK = 100

# Subrutin untuk menghitung total biaya berdasarkan jenis layanan
def HitungTotalBiaya(jenis, berat):
    if jenis == 'CUCI':
        harga_per_kg = 5000
    elif jenis == 'SETRIKA':
        harga_per_kg = 4000
    elif jenis == 'CUCI & SETRIKA':
        harga_per_kg = 8000
    else:
        harga_per_kg = 0
    return berat * harga_per_kg

# Subrutin memasukkan data transaksi awal
def IsiDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya):
    i = 0
    print(f'Data Transaksi Ke-{i+1}')
    print('------------------------------------')
    # Memasukkan Kode Transaksi pertama
    KodeTrk[i] = input('Kode Transaksi (isi "STOP" untuk selesai): ').upper()
    while (KodeTrk[i] != 'STOP' and i < MAKS_TRK):
        # Memasukkan data transaksi
        Nama[i] = input('Nama Pelanggan        : ').upper()
        JenisLayanan[i] = input('Jenis Layanan (Cuci/Setrika/Cuci & Setrika): ').upper()
        Berat[i] = float(input('Berat Cucian (kg)     : '))
        # Menghitung Total Biaya
        TotalBiaya[i] = HitungTotalBiaya(JenisLayanan[i], Berat[i])

        i += 1
        if i >= MAKS_TRK:
            print('Kapasitas data penuh!')
        print(f'\nData Transaksi Ke-{i+1}')
        print('------------------------------------')
        # Memasukkan Kode Transaksi berikutnya
        KodeTrk[i] = input('Kode Transaksi (isi "STOP" untuk selesai): ').upper()

    N = i
    return N

# Subrutin untuk menambahkan data transaksi baru
def TambahDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N):
    if N >= MAKS_TRK:
        print('Kapasitas data penuh! Tidak dapat menambahkan data baru.')
        return N
    print(f'\nData Transaksi Baru')
    print('------------------------------------')
    # Memasukkan data transaksi baru
    KodeTrk[N] = input('Kode Transaksi       : ').upper()
    Nama[N] = input('Nama Pelanggan       : ').upper()
    JenisLayanan[N] = input('Jenis Layanan (Cuci/Setrika/Cuci & Setrika): ').upper()
    Berat[N] = float(input('Berat Cucian (kg)    : '))
    # Menghitung Total Biaya
    TotalBiaya[N] = HitungTotalBiaya(JenisLayanan[N], Berat[N])
    print('Data transaksi berhasil ditambahkan.')
    N += 1
    return N

# Subrutin untuk menghapus data transaksi
def HapusDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N):
    kode_hapus = input('Masukkan Kode Transaksi yang akan dihapus: ').upper()
    index_hapus = -1
    for i in range(N):
        if KodeTrk[i] == kode_hapus:
            index_hapus = i
    if index_hapus == -1:
        print(f'Data dengan Kode Transaksi {kode_hapus} tidak ditemukan.')
    else:
        # Menggeser data untuk menimpa data yang dihapus
        for i in range(index_hapus, N - 1):
            KodeTrk[i] = KodeTrk[i + 1]
            Nama[i] = Nama[i + 1]
            JenisLayanan[i] = JenisLayanan[i + 1]
            Berat[i] = Berat[i + 1]
            TotalBiaya[i] = TotalBiaya[i + 1]
        # Mengosongkan data terakhir
        KodeTrk[N - 1] = ''
        Nama[N - 1] = ''
        JenisLayanan[N - 1] = ''
        Berat[N - 1] = 0
        TotalBiaya[N - 1] = 0
        print(f'Data dengan Kode Transaksi {kode_hapus} berhasil dihapus.')
        N -= 1
    return N

# Subrutin mengurutkan Nama secara ascending (Bubble Sort)
def SusunNamaAsc(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if Nama[j] > Nama[j + 1]:
                # Tukar Nama
                Nama[j], Nama[j + 1] = Nama[j + 1], Nama[j]
                # Tukar Kode Transaksi
                KodeTrk[j], KodeTrk[j + 1] = KodeTrk[j + 1], KodeTrk[j]
                # Tukar Jenis Layanan
                JenisLayanan[j], JenisLayanan[j + 1] = JenisLayanan[j + 1], JenisLayanan[j]
                # Tukar Berat
                Berat[j], Berat[j + 1] = Berat[j + 1], Berat[j]
                # Tukar Total Biaya
                TotalBiaya[j], TotalBiaya[j + 1] = TotalBiaya[j + 1], TotalBiaya[j]

# Subrutin menampilkan data transaksi
def TampilDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N):
    if N == 0:
        print('Belum ada data transaksi.')
        return
    print('\n                       DAFTAR TRANSAKSI LAUNDRY')
    print('----------------------------------------------------------------------------')
    print('| No | Kode Trk |     Nama Pelanggan     |   Jenis Layanan   | Berat | Biaya |')
    print('----------------------------------------------------------------------------')
    for i in range(N):
        print(f'| {i+1:>2} | {KodeTrk[i]:9} | {Nama[i]:22} | {JenisLayanan[i]:16} | {Berat[i]:>5.1f} | Rp{TotalBiaya[i]:>7,.0f} |')
    print('----------------------------------------------------------------------------')

# Subrutin mencari Kode Transaksi menggunakan Binary Search
def CariKodeTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N):
    # Pastikan data terurut berdasarkan Kode Transaksi
    SusunKodeTrkAsc(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
    KodeCari = input('Masukkan Kode Transaksi yang dicari: ').upper()
    Ia = 0
    Ib = N - 1
    Ketemu = False
    while (Ia <= Ib) and (not Ketemu):
        k = (Ia + Ib) // 2
        if KodeTrk[k] == KodeCari:
            Ketemu = True
        else:
            if KodeTrk[k] < KodeCari:
                Ia = k + 1
            else:
                Ib = k - 1

    os.system('cls')
    print('<< HASIL PENCARIAN >>')
    if Ketemu:
        print(f'Kode Transaksi : {KodeTrk[k]}')
        print(f'Nama Pelanggan : {Nama[k]}')
        print(f'Jenis Layanan  : {JenisLayanan[k]}')
        print(f'Berat Cucian   : {Berat[k]} kg')
        print(f'Total Biaya    : Rp{TotalBiaya[k]:,.0f}')
    else:
        print(f'Kode Transaksi {KodeCari} tidak ditemukan.')

# Subrutin mengurutkan Kode Transaksi secara ascending
def SusunKodeTrkAsc(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if KodeTrk[j] > KodeTrk[j + 1]:
                # Tukar Kode Transaksi
                KodeTrk[j], KodeTrk[j + 1] = KodeTrk[j + 1], KodeTrk[j]
                # Tukar Nama
                Nama[j], Nama[j + 1] = Nama[j + 1], Nama[j]
                # Tukar Jenis Layanan
                JenisLayanan[j], JenisLayanan[j + 1] = JenisLayanan[j + 1], JenisLayanan[j]
                # Tukar Berat
                Berat[j], Berat[j + 1] = Berat[j + 1], Berat[j]
                # Tukar Total Biaya
                TotalBiaya[j], TotalBiaya[j + 1] = TotalBiaya[j + 1], TotalBiaya[j]

# Subrutin mencari Nama Pelanggan menggunakan Sequential Search
def CariNamaPelanggan(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N):
    NamaCari = input('Masukkan Nama Pelanggan yang dicari: ').upper()
    ditemukan = False
    print('<< HASIL PENCARIAN >>')
    for i in range(N):
        if Nama[i] == NamaCari:
            if not ditemukan:
                print('\nData ditemukan:')
                print('------------------------------------------------------------------------------------')
                print('| No | Kode Transaksi |     Nama Pelanggan     |   Jenis Layanan   | Berat | Biaya |')
                print('------------------------------------------------------------------------------------')
                ditemukan = True
            print(f'| {i+1:>2} |    {KodeTrk[i]:9}    | {Nama[i]:22} | {JenisLayanan[i]:16} | {Berat[i]:>5.1f} | Rp{TotalBiaya[i]:>7,.0f} |')
    if not ditemukan:
        print(f'Nama Pelanggan {NamaCari} tidak ditemukan.')
    else:
        print('----------------------------------------------------------------------------')

# Subrutin penghancuran data transaksi
def HancurDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N):
    konfirmasi = input('Anda yakin ingin menghancurkan data transaksi [Y/T]? ').upper()
    if konfirmasi == "Y":
        for i in range(N):
            KodeTrk[i] = ''
            Nama[i] = ''
            JenisLayanan[i] = ''
            Berat[i] = 0
            TotalBiaya[i] = 0
        N = 0
        print('Data transaksi berhasil dihancurkan.')
    else:
        print('Data transaksi tidak dihancurkan.')
    return N

# Badan Program Utama

os.system('cls')

# Inisialisasi array untuk data transaksi
KodeTrk = [''] * MAKS_TRK
Nama = [''] * MAKS_TRK
JenisLayanan = [''] * MAKS_TRK
Berat = [0] * MAKS_TRK
TotalBiaya = [0] * MAKS_TRK

# Memasukkan data transaksi
print('<< PENGISIAN DATA TRANSAKSI LAUNDRY >>')
N = IsiDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya)

os.system('cls')
print('<< DATA SEBELUM TERURUT >>')
TampilDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
os.system('pause')

# Menu Operasi
Lagi = 'Y'
while Lagi != 'T':
    os.system('cls')
    print('MENU TRANSAKSI LAUNDRY')
    print('----------------------')
    print('1. Tampilkan Data Transaksi')
    print('2. Urutkan Data Berdasarkan Nama Pelanggan')
    print('3. Cari Kode Transaksi')
    print('4. Cari Nama Pelanggan') 
    print('5. Tambah Data Transaksi')
    print('6. Hapus Data Transaksi')
    print('7. Hancur Data Transaksi')
    Pilih = int(input('Pilihan Anda? '))
    os.system('cls')
    match (Pilih):
        case 1:
            print('<< DATA TRANSAKSI LAUNDRY >>')
            TampilDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
            os.system('pause')
        case 2:
            print('<< DATA SETELAH TERURUT BERDASARKAN NAMA PELANGGAN >>')
            SusunNamaAsc(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
            TampilDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
            os.system('pause')
        case 3:
            print('<< PENCARIAN KODE TRANSAKSI >>')
            CariKodeTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
            os.system('pause')
        case 4:
            print('<< PENCARIAN NAMA PELANGGAN >>')
            CariNamaPelanggan(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
            os.system('pause')
        case 5:
            print('<< PENAMBAHAN DATA TRANSAKSI >>')
            N = TambahDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
            os.system('pause')
        case 6:
            print('<< PENGHAPUSAN DATA TRANSAKSI >>')
            N = HapusDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
            os.system('pause')
        case 7:
            print('<< PENGHANCURAN DATA TRANSAKSI >>')
            N = HancurDataTrk(KodeTrk, Nama, JenisLayanan, Berat, TotalBiaya, N)
            os.system('pause')
        case _:
            print('Pilihan tidak valid.')
            os.system('pause')

    print()
    Lagi = input('Mau melakukan operasi lain [Y/T]? ').upper()
