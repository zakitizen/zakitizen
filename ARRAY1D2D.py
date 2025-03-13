#program aaray 1 dimensi dan 2 dimensi
#I.S.: Pengguna memeilihsalah satu menu
#F.S.: menampilkan menu sesuai yang dipilih
import os

#konstanta
MaksAngka = 10
MaksBaris = 5
MaksKolom = 3

#subrutin menu utama
def MenuUtama(Pilih):
    print('<< Menu utama >>')
    print('1. Array 1 Dimensi')
    print('2. Array 2 Dimensi')
    print('0. Keluar')
    Pilih = int(input('Masukkan pilihan menu anda : '))
    while (Pilih < 0 ) and (Pilih > 2):
        print('Menu tidak ada, tekan enter untuk memasukkan ulang')
        Pilih = int(input('Masukkan pilihan menu anda : '))
    return Pilih

#subrutin menu array 1 dimensi
def MenuArray1D(Pilih1):
    print('<< MENU ARRAY 1 DIMENSI >>')
    print('1. Pengisian elemen array angka')
    print('2. Penambahan elemen array angka')
    print('3. Penyisipan elemen array angka')
    print('4. Penghapusan elemen array angka')
    print('5. Penyajian elemen array angka')
    print('0. kembali ke menu utama')
    Pilih1 = int(input('Masukkan pilihan menu anda : '))
    while (Pilih1 < 0 ) and (Pilih1 > 5):
        print('Menu tidak ada, tekan enter untuk memasukkan ulang')
        Pilih1 = int(input('Masukkan pilihan menu anda : '))
    return Pilih1

#subrutin memeasukan elemen array angka
def IsiAngka(Angka, BanyakData):
    for i in range(BanyakData):
        Angka[i] = int(input(f'Angka ke-{i+1} :'))
        
        
def SisipAngka(Angka, BanyakData, PosisiSisip, AngkaBaru):
    if (BanyakData < MaksAngka):
        if (PosisiSisip >= 1) and (PosisiSisip <= BanyakData):
            for i in range (BanyakData, PosisiSisip):
                Angka[i + 1] = Angka[i]
            Angka[PosisiSisip] = AngkaBaru
            BanyakData = BanyakData + 1
        else:
            print('Posisi sisip tidak valid')
    else:
        print('Data Penuh')

def TambahAngka(Angka, BanyakData, AngkaBaru):
    if (BanyakData < MaksAngka):
        Angka[BanyakData] = AngkaBaru
        print(f'angka = {AngkaBaru} berhasil ditambahkan di posisi ke-{BanyakData+1}')
    else:
        os.system('cls')
        print('data sudah penuh')

def HapusAngka(Angka, BanyakData, PosisiHapus):
    if (BanyakData > 0):
        if (PosisiHapus >= 1) and (PosisiHapus <= BanyakData):
            for i in range (PosisiHapus, BanyakData):
                Angka[i - 1] = Angka[i]
            Angka[BanyakData] = 0

#subrutin menampilkan elem array angka
def TampilAngka(Angka, BanyakData):
    for i in range (BanyakData):
        print(f'Angka Ke-[{i+1}] =  {Angka[i]}')

#subrutin menu array 2 dimensi
def MenuArray2D(Pilih2):
    print('<< MENU ARRAY 2 DIMENSI >>')
    print('1. Pengisian elemen matriks A')
    print('2. Pengubahan elemen matriks A')
    print('3. Penghapusan elemen matriks A')
    print('4. Penyajian elemen matriks A')
    print('0. kembali ke menu utama')
    Pilih2 = int(input('Masukkan pilihan menu anda : '))
    while (Pilih2 < 0 ) and (Pilih2 > 5):
        print('Menu tidak ada, tekan enter untuk memasukkan ulang')
        Pilih2 = int(input('Masukkan pilihan menu anda : '))
    return Pilih2

#subrutin penciptaan matriks
def PenciptaanMatriks(A):
    for j in range (MaksBaris):
        A[j] = [0] * MaksKolom
        
#subrutin memeasukan elemen array matriks A
def IsiMatriks(A):
    for i in range(MaksBaris):
        for j in range (MaksKolom):
            A[i][j] = int(input(f'A [{i+1},{j+2}] :'))
            
#subrutin ubah elemen matriks A
def UbahElemen(A, ElemenBaru, PosisiBaris, PosisiKolom):
    if (PosisiBaris-1 >= 0) and (PosisiKolom-1 <= MaksBaris-1 ):
        if (PosisiKolom-1 >= 0) and (PosisiKolom-1 <= MaksKolom-1 ):
            A[PosisiBaris-1][PosisiKolom-1] = ElemenBaru
            print(f'Baris {PosisiBaris} Kolom {PosisiKolom} berhasil diubah menjadi {ElemenBaru}')

def HapusElemen(A, PosisiBaris, PosisiKolom):
    if (PosisiBaris >= 1) and (PosisiBaris <= MaksBaris):
        if (PosisiKolom >= 1) and (PosisiKolom <= MaksKolom):
            ElemenHapus = A[PosisiBaris - 1][PosisiKolom - 1]  # Sesuaikan indeks ke 0-based
            A[PosisiBaris - 1][PosisiKolom - 1] = 0  # Set elemen menjadi 0
            print(f'Elemen yang dihapus: {ElemenHapus}')
        else:
            print('Posisi kolom tidak sesuai')
    else:
        print('Posisi baris tidak sesuai')
        
#subrutin menampilkan elem array matriks A
def TampilMatriks(A):
    for i in range (MaksBaris):
        for j in range (MaksKolom):
            print(f'    {A[i][j]:>2}', end='    ')
        print()

#badan program utama
os.system('cls')
Pilih = 0
Pilih = MenuUtama(Pilih)
while (Pilih != 0):
    os.system('cls')
    match (Pilih) :
        case 1 :
            Pilih1 = 0
            Pilih1 = MenuArray1D(Pilih1)
            #penciptaan array angka
            Angka = [0] * MaksAngka
            while(Pilih1 != 0 ):
                os.system('cls')
                match (Pilih1) :
                    case 1 :
                        print('1. Pengisian array angka')
                        BanyakData = int(input('Banyak data yang diolah : '))
                        IsiAngka(Angka, BanyakData)
                    case 2 : 
                        print('2. Penambahan array angka')
                        AngkaBaru = int(input('Angka yang ditambahkan :'))
                        TambahAngka(Angka, BanyakData, AngkaBaru)
                        BanyakData = BanyakData + 1
                    case 3 :
                        print('3. Penyisipan array angka')
                        PosisiSisip = int(input('Masukkan posisi yang ingin diganti : '))
                        AngkaBaru = int(input('Masukkan angka baru : '))
                        SisipAngka(Angka, BanyakData, PosisiSisip, AngkaBaru)
                    case 4 : 
                        print('4. Penghapusan array angka')
                        PosisiHapus = int(input('Masukkan posisi array yang ingin di hapus : '))
                        HapusAngka(Angka, BanyakData, PosisiHapus)
                        BanyakData = BanyakData - 1
                    case 5 : 
                        print('5. Penyajian array angka')
                        TampilAngka(Angka, BanyakData)
                os.system('pause')
                os.system('cls')
                Pilih1 = MenuArray1D(Pilih1)
        case 2 :
            Pilih2 = 0
            Pilih2 = MenuArray2D(Pilih2)
            #Penciptaan matriks A
            A = [0] * MaksBaris
            PenciptaanMatriks(A)
            while(Pilih2 != 0 ):
                os.system('cls')
                match (Pilih2) :
                    case 1 :
                        print('1. Pengisian elemen matriks A')
                        IsiMatriks(A)
                    case 2 :
                        print('2. Pengubahan elemen matriks A')
                        ElemenBaru = int(input('Elemen baru : '))
                        PosisiBaris = int(input('Posisi baris : '))
                        PosisiKolom = int(input('Posisi kolom : '))
                        UbahElemen(A, ElemenBaru, PosisiBaris, PosisiKolom)
                    case 3 :
                        print('3. Penghapusan elemen matriks A')
                        PosisiBaris = int(input('Posisi baris : '))
                        PosisiKolom = int(input('Posisi kolom : '))
                        HapusElemen(A, PosisiBaris, PosisiKolom)
                    case 4 :
                        print('4. Penyajian elemen matriks A')
                        TampilMatriks(A)
                os.system('pause')
                os.system('cls')
                Pilih2 = MenuArray2D(Pilih2)
    
    os.system('cls')
    Pilih = MenuUtama(Pilih)