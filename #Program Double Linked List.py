#Program Double Linked List
#I.S.: diberikan harga awal terhadap pointer kepala(awal,akhir)
#F.S.: menampilkan isi list
import os

#pendefinisian double linked list
#1. membuat kelas untuk data mahasiswa
class Mhs:
    def __init__(self,NIM,Nama,NA,Indeks):
        self.NIM = NIM
        self.Nama = Nama
        self.NA = NA
        self.Indeks = Indeks

#2. membuat kelas untuk simpul
class Node:
    def __init__(self,NIM,Nama,NA,Indeks):
        self.Info = Mhs(NIM,Nama,NA,Indeks)
        self.Prev = None
        self.Next = None

#3. membuat kelas untuk linked list
class DoubleLinkedList:
    def __init__(self):
        self.Awal = None
        self.Akhir = None

    #method mengecek list kosong atau tidak
    def Kosong(self):
        return self.Awal is None
    
    #method mengecek list berisi satu simpul atau lebih
    def SatuNode(self):
        return self.Awal is self.Akhir
    
    #method menentukan indeks nilai
    def IndeksNilai(self,NA):
        if (78<=NA<=100):
            return 'A'
        elif (68<=NA<=78):
            return 'B'
        elif (56<=NA<=68):
            return 'C'
        elif (45<=NA<=56):
            return 'D'
        else:
            return 'E'
        

    
    #method menambah satu simpul di belakang
    def SisipBelakangDouble(self,MhsBaru):
        Baru = Node(MhsBaru.NIM,MhsBaru.Nama,MhsBaru.NA,MhsBaru.Indeks)
        Baru.Next = None
        if (self.Kosong()):
            Baru.Prev = None
            self.Awal = Baru
        else:
            Baru.Prev = self.Akhir
            self.Akhir.Next = Baru
        
        self.Akhir = Baru
    
    #method menampilkan isi list
    def TampilData(self):
        print('<< ISI LINKED LIST >>')
        if (self.Kosong()):
            print('List Kosong')
        else:
            Bantu = self.Awal
            while (Bantu is not None):
                print(f'[{Bantu.Info.NIM}|{Bantu.Info.Nama}|{Bantu.Info.NA:.1f}|{Bantu.Info.Indeks}]',end='')
                if (Bantu is not self.Akhir ):
                    print(' --> ',end='')

                Bantu = Bantu.Next

            print()

    #method mencari indeks nilai tertentu
    def CariIndeks(self):
        if (self.Kosong()):
            print('List masih kosong')
        else:
            IndeksMin = str(input('Indeks yang dicari minimal  :')).upper()
            IndeksMax = str(input('Indeks yang dicari maksimal :')).upper()
            Bantu = self.Awal
            Ketemu = False
            while (not Ketemu) and (Bantu is not None):
                if(IndeksMin<=Bantu.Info.Indeks<=IndeksMax):
                    Ketemu = True
                else:
                    Bantu = Bantu.Next

            if (Ketemu):
                os.system('cls')
                print('         << DAFTAR NILAI MAHASISWA >>')
                print(f'(Indeks Nilai {IndeksMin} sampai {IndeksMax})')
                print('-------------------------------------------')
                print('| No |    NIM    | Nama Mahasiswa | Nilai |')
                print('-------------------------------------------')
                No = 0
                Bantu2 = Bantu
                while (Bantu2 is not None):
                    if(IndeksMin<=Bantu.Info.Indeks<=IndeksMax):
                        No += 1
                        print(f'| {No:2} | {Bantu2.Info.NIM:9} | {Bantu2.Info.Nama:14} | {Bantu2.Info.NA:5.1f} |')
                Bantu2 = Bantu2.Next
                print('-------------------------------------------')
            else:
                print(f'Indeks Nilai {IndeksMin} sampai {IndeksMax} tidak ada!')


    #method menghapus satu simpul di depan
    def HapusDepanDouble(self):
        if (self.Kosong()):
            print('List masih kosong')
        else:
            Phapus = self.Awal
            MhsHapus = Phapus.Info
            if (self.SatuNode()):
                self.Awal = None
                self.Akhir = None
            else:
                self.Awal = Phapus.Next
                self.Awal.Prev = None

            del(Phapus)
            #menampilkan data mahasiswa yang sudah dihapus
            print('<< DATA MAHASISWA YANG SUDAH DIHAPUS >>')
            print(f'NIM            : {MhsHapus.NIM}')
            print(f'Nama Mahasiswa : {MhsHapus.Nama}')
            print(f'Nilai Akhir    : {MhsHapus.NA:.1f}')
            print(f'Indeks Nilai   : {MhsHapus.Indeks}')

    #method menyusun NIM secara ascending
    def UrutNIMAsc(self):
        if (self.Kosong()):
            print('List masih kosong')
        else:
            i = self.Awal
            while (i is not self.Akhir):
                j = self.Akhir
                while (j is not i):
                    if (j.Info.NIM < j.Prev.Info.NIM):
                        #pertukaran data
                        Temp = j.Info
                        j.Info = j.Prev.Info
                        j.Prev.Info = Temp
                        
                    j = j.Prev

                i = i.Next
    #method menyusun NIM secara descending
    def UrutNIMDsc(self):
        if (self.Kosong()):
            print('List masih kosong')
        else:
            i = self.Awal
            while (i is not self.Akhir):
                j = self.Akhir
                while (j is not i):
                    if (j.Info.NIM > j.Prev.Info.NIM):
                        #pertukaran data
                        Temp = j.Info
                        j.Info = j.Prev.Info
                        j.Prev.Info = Temp
                        
                    j = j.Prev

                i = i.Next
            

    #method menghapus seluruh simpul
    def Penghancuran(self):
        Phapus = self.Awal
        while (not self.Kosong()):
            self.Awal = Phapus.Next
            if (self.Awal is not None):
                self.Awal.Prev = None

            del(Phapus)
            Phapus = self.Awal

        self.Akhir = None


#badan program utama
#inisialisasi linked list
List = DoubleLinkedList()

#inisialisasi data mahasiswa
NIM = '/'
Nama = '/'
NA = 0
Indeks = '/'
MhsBaru = Mhs(NIM,Nama,NA,Indeks)

#memasukkan data mahasiswa
Lagi = 'Y'
while (Lagi != 'T'):
    os.system('cls')
    print('<< PENGISIAN DATA MAHASISWA BARU >>')
    MhsBaru.NIM  = str(input('NIM            : '))
    MhsBaru.Nama = str(input('Nama Mahasiswa : '))
    MhsBaru.NA   = float(input('Nilai Akhir    : '))
    MhsBaru.Indeks = List.IndeksNilai(MhsBaru.NA)
    print(f'Indeks Nilai   : {MhsBaru.Indeks}')
    List.SisipBelakangDouble(MhsBaru)
    print()
    List.TampilData()
    print()
    Lagi = str(input('Mau Tambah Data Lagi [Y/T]? ')).upper()

os.system('cls')
MauHapus = str(input('Mau Hapus Data [Y/T]? ')).upper()
if (MauHapus == 'Y'):
    Lagi = 'Y'
    while (Lagi != 'T') and (not List.Kosong()):
        os.system('cls')
        List.HapusDepanDouble()
        print()
        List.TampilData()
        print()
        Lagi = str(input('Mau Hapus Data Lagi [Y/T]? ')).upper()

os.system('cls')
MauCari = str(input('Mau Cari Indeks Nilai [Y/T]? ')).upper()
if (MauCari == 'Y'):
    Lagi = 'Y'
    while (Lagi != 'T'):
        os.system('cls')
        List.CariIndeks()
        print()
        Lagi = str(input('Mau Cari Indeks Nilai Lagi [Y/T]? ')).upper()

os.system('cls')
print('NIM SEBELUM TERURUT')
print('===================')
List.TampilData()
print()
print('NIM SETELAH TERURUT SECARA ASCENDING')
print('====================================')
List.UrutNIMAsc()
List.TampilData()
os.system('pause')
print()
print('NIM SETELAH TERURUT SECARA DESCENDING')
print('====================================')
List.UrutNIMDsc()
List.TampilData()
os.system('pause')

List.Penghancuran()
os.system('cls')
List.TampilData()