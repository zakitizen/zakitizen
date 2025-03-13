#Program Pengolahan Data Nilai Mahasiswa
#I.S.: penggunqa memasukkan NIM, nama mahasiswa (Nama), dan nilai akhir (NA)
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



#subrutin memasukkan data nilai mahasiswa
def IsiDataMhs(NIM,Nama,NA,Indeks):
    i = 0
    print(f'Data Nilai Mahasiswa Ke-{i+1}')
    print(f'-----------------------------')
    #memasukkan NIM pertama
    NIM[i] = str(input('Nomor Induk Mahasiswa : ')).upper()
    while (NIM[i] != 'STOP'):
        #memasukkan nama mahasiswa dan nilai akhir
        Nama[i] = str(input('Nama Mahasiswa      : ')).upper()
        NA[i]   = float(input('Nilai Akhir         : '))

        #memanggil fungsi indeks nilai
        Indeks[i] = IndeksNilai(NA[i])

        i = i + 1
        print()
        print(f'Data Nilai Mahasiswa Ke-{i+1}')
        print(f'-----------------------------')
        #memasukkan NIM berikutnya
        NIM[i] = str(input('Nomor Induk Mahasiswa : ')).upper()
    N = i
    return N
#subrutin mengurutkan NIM secara ascending (Bubble sort)
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

                #tukar NA
                Temp = NA[j]
                NA[j] = NA[j-1]
                NA[j-1] = Temp

                #tukar Indeks
                Temp = Indeks[j]
                Indeks[j] = Indeks[j-1]
                Indeks[j-1] = Temp
            j -= 1 

#subrutin mengurutkan nama secara descending
def SusunNamaDsc(NIM,Nama,NA,Indeks,N):
    for i in range(N-1):
        for j in range(N-(i+1)):
            if (Nama[j] < Nama[j+1]):
                #tukar NIM
                Temp = NIM[j]
                NIM[j] = NIM[j+1]
                NIM[j+1] = Temp

                #tukar Nama
                Temp = Nama[j]
                Nama[j] = Nama[j+1]
                Nama[j-1] = Temp

                #tukar NA
                Temp = NA[j]
                NA[j] = NA[j+1]
                NA[j-1] = Temp

                #tukar Indeks
                Temp = Indeks[j]
                Indeks[j] = Indeks[j+1]
                Indeks[j+1] = Temp

#subrutin mengurutkan nilai (NA) secara ascending (Maximum Sort)
def SusunNilaiAsc(NIM,Nama,NA,Indeks,N):
    for i in range(N-1):
        max = 0
        for j in range(1,N+1-(i+1)):
            if (NA[j] > NA[max]):
                max = j
        #tukar NIM
        Temp = NIM[j]
        NIM[j] = NIM[max]
        NIM[max] = Temp

        #tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[max]
        Nama[max] = Temp

        #tukar NA
        Temp = NA[j]
        NA[j] = NA[max]
        NA[max] = Temp

        #tukar Indeks
        Temp = Indeks[j]
        Indeks[j] = Indeks[max]
        Indeks[max] = Temp

#subrutin mengurutkan indeks nilai secara ascending (Minimum Sort)
def SusunIndeksAsc(NIM,Nama,NA,Indeks,N):
    for i in range(N-1):
        min = i
        for j in range(min+1,N):
            if (Indeks[j] < Indeks[min]):
                min = j
        #tukar NIM
        Temp = NIM[j]
        NIM[j] = NIM[min]
        NIM[min] = Temp

        #tukar Nama
        Temp = Nama[j]
        Nama[j] = Nama[min]
        Nama[min] = Temp

        #tukar NA
        Temp = NA[j]
        NA[j] = NA[min]
        NA[min] = Temp

        #tukar Indeks
        Temp = Indeks[j]
        Indeks[j] = Indeks[min]
        Indeks[min] = Temp
            

#subrutin menampilkan daftar nilai mahasiswa
def TampilDataMhs(NIM,Nama,NA,Indeks,Kelas,MK,N):
    print('                  DAFTAR NILAI MAHASISWA')
    print(f'Kelas            : {Kelas} ')
    print(f'Mata Kuliah      : {MK} ')
    print('----------------------------------------------------------')
    print('| NO |    NIM    |    Nama Mahasiswa    | Nilai | Indeks |')
    print('----------------------------------------------------------')
    for i in range (N):
        print(f'| {i+1:2} | {NIM[i]:9} | {Nama[i]:20} | {NA[i]:5.1f} |   {Indeks[i]:1}    |')

    print('----------------------------------------------------------')

#badan program
os.system('cls')
#penciptaan array nim, nama mahasiswa, nilai akhir, danindeks nilai
NIM = ['/'] * MAKSMHS
Nama = ['/'] * MAKSMHS
NA = [0] *MAKSMHS
Indeks = ['/'] * MAKSMHS

#memasukkan kelas dan nama matakuliah
print('<< PENGISIAN NILAI DATA MAHASISWA>>')
Kelas = str(input('Kelas     : '))
MK = str(input('Mata Kuliah  : '))
#memasukkan data nilai mahasiswa
N = IsiDataMhs(NIM,Nama,NA,Indeks)


os.system('cls')
print('<< DATA SEBELUM TERURUT >>')
TampilDataMhs(NIM,Nama,NA,Indeks,Kelas,MK,N)
os.system('pause')

print('<< NIM TERURUT SECARA ASCENDING(BUBBLE SORT) >>')
SusunNIMAsc(NIM,Nama,NA,Indeks,N)
TampilDataMhs(NIM,Nama,NA,Indeks,Kelas,MK,N)
os.system('pause')


print('<< NAMA TERURUT SECARA DESCENDING(BUBBLE SORT) >>')
SusunNamaDsc(NIM,Nama,NA,Indeks,N)
TampilDataMhs(NIM,Nama,NA,Indeks,Kelas,MK,N)
os.system('pause')


print('<< NILAI TERURUT SECARA ASCENDING(MAXIMUM SORT) >>')
SusunNilaiAsc(NIM,Nama,NA,Indeks,N)
TampilDataMhs(NIM,Nama,NA,Indeks,Kelas,MK,N)
os.system('pause')

print('<< INDEKS TERURUT SECARA ASCENDING(MINIMUM SORT) >>')
SusunIndeksAsc(NIM,Nama,NA,Indeks,N)
TampilDataMhs(NIM,Nama,NA,Indeks,Kelas,MK,N)



