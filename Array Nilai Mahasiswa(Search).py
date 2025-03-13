#Program Pengolahan Data Nilai Mahasiswa
#I.S.: pengguna memasukkan array NIM, nama mahasiswa dan nilai (1:N)
#F.S.: menampilkan data nilai mahasiswa (1:N) yang sudah terurut
import os

#konstanta
MAKSMHS = 10

#subrutin menentukan indeks nilai
def IndeksNilai(Nilai):
    if (80<=Nilai<=100):
        return 'A'
    elif (70<=Nilai<80):
        return 'B'
    elif (60<=Nilai<70):
        return 'C'
    elif (50<=Nilai<60):
        return 'D'
    else:
        return 'E'

#subrutin memasukkan elemen array NIM, nama mahasiswa dan nilai akhir
def IsiDataMhs(NIM,Nama,NA,Indeks):
    i = 0
    print()
    print(f'Data Nilai Mahasiswa Ke-{i+1}')
    print(f'--------------------------')
    #memasukkan elemen NIM pertama
    NIM[i] = str(input('Nomor Induk Mahasiswa : ')).upper()
    while (NIM[i] != 'STOP'):
        #memasukkan nama mahasiswa dan nilai akhir
        Nama[i] = str(input('Nama Mahasiswa        : ')).upper()
        NA[i]   = float(input('Nilai Akhir           : '))
        #validasi nilai akhir

        Indeks[i] = IndeksNilai(NA[i])

        #memasukkan elemen NIM berikutnya
        i = i + 1
        print()
        print(f'Data Nilai Mahasiswa Ke-{i+1}')
        print(f'--------------------------')
        #memasukkan elemen NIM berikutnya
        NIM[i] = str(input('Nomor Induk Mahasiswa : ')).upper()

    N = i
    return N

#subrutin menampilkan data nilai mahasiswa
def TampilDataMhs(NIM,Nama,NA,Indeks,Kelas,MatKul,N):
    print('                  DAFTAR NILAI MAHASISWA')
    print(f'Kelas       : {Kelas}')
    print(f'Mata Kuliah : {MatKul}')
    print('----------------------------------------------------------')
    print('| No |    NIM    |    Nama Mahasiswa    | Nilai | Indeks |')
    print('----------------------------------------------------------')
    for i in range(N):
        print(f'| {i+1:>2} | {NIM[i]:9} | {Nama[i]:20} | {NA[i]:>5.1f} |   {Indeks[i]:1}    |')

    print('----------------------------------------------------------')

#subrutin mengurutkan NIM secara ascending (Bubble Sort)
def SusunNIMAsc(NIM,Nama,NA,Indeks,N):
    for i in range(N-1):
        j = N
        while (j >= i+1):
            if (NIM[j] < NIM[j-1]):
                #tukar NIM
                Temp = NIM[j]
                NIM[j] = NIM[j-1]
                NIM[j-1] = Temp

                #tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j-1]
                Nama[j-1] = Temp

                #tukar Nilai Akhir
                Temp = NA[j]
                NA[j] = NA[j-1]
                NA[j-1] = Temp

                #tukar Indeks
                Temp = Indeks[j]
                Indeks[j] = Indeks[j-1]
                Indeks[j-1] = Temp

            j -= 1 #j = j - 1 

#SUBRUTIN MENCARI NIM TERTENTU MENGGUNAKAN BINARY SEARCH TERURUT ASC
def CariNIM(NIM,Nama,NA,Indeks,N):
    #MEMASUKKAN NIM YANG DICARI
    NIMCari = str(input("NIM yang dicari :"))
    #PROSES PENCARIAN
    Ia = 0
    Ib = N - 1
    Ketemu = False
    while not Ketemu and Ia <= Ib:
        #MENGHITUNG POSISI TENGAH
        k = (Ia + Ib) // 2
        if NIM[k] == NIMCari:
            Ketemu = True
        else:
            if NIM[k] < NIMCari:
                #PENCARIAN DILANJUTKAN KE BAGIAN KANAN
                Ia = k + 1
            else:
                #PENCARIAN DILANJUTKAN KE BAGIAN KIRI
                Ib = k - 1

                

    os.system('cls')
    print("<<HASIL PENCARIAN>>")
    if Ketemu:
        print(f"NIM yang dicari : {NIMCari}")
        print(f"Nama mahasiswa  : {Nama[k]}")    
        print(f"Nilai akhir     : {NA[k]}")    
        print(f"Indeks nilai    : {Indeks[k]}")
    else:
        print(f"NIM {NIMCari} tidak ditemukan!")    
        
#SUBRUTIN MENCARI NIM TERTENTU MENGGUNAKAN BINARY SEARCH TERURUT ASC
def CariNilai(NIM,Nama,NA,Indeks,N):
    #MEMASUKKAN NILAI AKHIR YANG DICARI
    NACariMin = float(input("Nilai yang dicari (MINIMAL)  :"))
    NACariMax = float(input("Nilai yang dicari (MAKSIMAL) :"))

    #PROSES PENCARIAN
    i = 0
    Ketemu = False
    while not Ketemu and i <= N:
        if NA[i] >= NACariMin and NA[i] <= NACariMax:
            Ketemu = True
        else:
           i += 1

                

    os.system('cls')
    print("<<HASIL PENCARIAN>>")
    if Ketemu:
        print('                  DAFTAR NILAI MAHASISWA')
        print(f'Kelas       : {Kelas}')
        print(f'Mata Kuliah : {MatKul}')
        print(f'Nilai Akhir : {NACariMin} - {NACariMax}')
        print('----------------------------------------------------------')
        print('| No |    NIM    |    Nama Mahasiswa    | Nilai | Indeks |')
        print('----------------------------------------------------------')
        No = 0
        for j in range(i,N):
            if NA[j] >= NACariMin and NA[j] <= NACariMax:
                No += 1
                print(f'| {No:>2} | {NIM[j]:9} | {Nama[j]:20} | {NA[j]:>5.1f} |    ')

        print('----------------------------------------------------------')
    else:
        print(f"NIM {NACariMin} - {NACariMax} tidak ditemukan!") 

#SEQUENTIAL SEARCH TANPA SENTINEL
def CariIndeks(NIM,Nama,NA,Indeks,N):
    #MEMASUKKAN INDEKS YANG DICARI
    IndeksCariMin = str(input("Indeks yang dicari (MINIMAL)  :"))
    IndeksCariMax = str(input("Indeks yang dicari (MAKSIMAL) :"))

    #PROSES PENCARIAN
    i = 0
    while ((Indeks[i] < IndeksCariMin or Indeks[i] > IndeksCariMax)) and i < N:
           i += 1

                

    os.system('cls')
    print("<<HASIL PENCARIAN>>")
    if (Indeks[i] >= IndeksCariMin and Indeks[i] <= IndeksCariMax):
        print('                  DAFTAR NILAI MAHASISWA')
        print(f'Kelas       : {Kelas}')
        print(f'Mata Kuliah : {MatKul}')
        print(f'Nilai Akhir : {IndeksCariMin} - {IndeksCariMax}')
        print('----------------------------------------------------------')
        print('| No |    NIM    |    Nama Mahasiswa    | Nilai | Indeks |')
        print('----------------------------------------------------------')
        No = 0
        for j in range(i,N):
            if Indeks[j] >= IndeksCariMin and Indeks[j] <= IndeksCariMax:
                No += 1
                print(f'| {No:>2} | {NIM[j]:9} | {Nama[j]:20} | {NA[j]:>5.1f} |    ')

        print('----------------------------------------------------------')
    else:
        print(f"NIM {IndeksCariMin} - {IndeksCariMax} tidak ditemukan!") 


#badan program utama
os.system('cls')
#penciptaan array NIM, nama mahasiswa (Nama), nilai akhir (NA) dan Indeks
NIM  = ['/'] * MAKSMHS
Nama = ['/'] * MAKSMHS
NA = [0] * MAKSMHS
Indeks = ['/'] * MAKSMHS

#memasukkan kelas dan nama mata kuliah
print('<<PENGISIAN DATA NILAI MAHASISWA>>')
Kelas  = str(input('Kelas       : '))
MatKul = str(input('Mata Kuliah : '))
N = IsiDataMhs(NIM,Nama,NA,Indeks)

os.system('cls')
#memanggil subrutin tampil data nilai
print('<<DATA NILAI SEBELUM TERURUT>>')
TampilDataMhs(NIM,Nama,NA,Indeks,Kelas,MatKul,N)
os.system('pause')

Lagi = 'Y'
while Lagi != "T":
    os.system('cls')
    print("MENU PENCARIAN")
    print("--------------")
    print('1. Cari NIM')#METODENYA BINARY
    print('2. Cari Nilai Akhir')#MEQUENTIAL SEARCH BOOLEAN
    print('3. Cari Indeks Nilai')#
    Pilih = int(input("Pilihan anda :"))
    os.system('cls')
    match (Pilih):
        case 1 :
            print("<PENCARIAN NIM TERTENTU>")
            SusunNIMAsc(NIM,Nama,NA,Indeks,N)
            CariNIM(NIM,Nama,NA,Indeks,N)
        case 2 :
            print("<PENCARIAN NILAI AKHIR TERTENTU>")
            CariNilai(NIM,Nama,NA,Indeks,N)
        case 3 :
            print("<PENCARIAN NILAI INDEKS TERTENTU>")
            CariIndeks(NIM,Nama,NA,Indeks,N)

    print("")
    Lagi = str(input("Mau coba lagi (Y/T) :")).upper()
    
