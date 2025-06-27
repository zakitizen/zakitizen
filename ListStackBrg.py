#Program Linked List Stack Barang
#I.S.: diberikan harga awal terhadap pointer kepala (top)
#F.S.: menampilkan isi list stack barang
import os

#pendefinisian list stack barang
#1. membuat kelas untuk record barang
class DataBarang:
    def __init__(self,KodeBrg,NamaBrg,Stok,Status):
        self.KodeBrg = KodeBrg
        self.NamaBrg = NamaBrg
        self.Stok = Stok
        self.Status = Status

#2. membuat kelas untuk simpul barang
class NodeBrg:
    def __init__(self,KodeBrg,NamaBrg,Stok,Status):
        self.Brg = DataBarang(KodeBrg,NamaBrg,Stok,Status)
        self.Prev = None
        self.Next = None      

#3. membuat kelas untuk linked list stack barang
class ListBarang:
    def __init__(self):
        self.Top = None

    #method mengecek stack kosong atau tidak
    def Kosong(self):
        return self.Top is None
    
    #method mengecek stack satu simpul atau lebih
    def SatuSimpul(self):
        return self.Top.Next is None

    #method menentukan status stok
    def StatusStok(self,Stok):
        if (Stok > 0):
            return 'Aman'
        else:
            return 'Tidak Aman'
        
    #method menambah satu data ke stack (sisip depan)--> Push
    def PushBrg(self,BrgMasuk):
        Baru = NodeBrg(BrgMasuk.KodeMasuk,BrgMasuk.NamaMasuk,BrgMasuk.StokMasuk,BrgMasuk.StatusMasuk)
        Baru.Prev = None
        if (self.Kosong()):
            Baru.Next = None
        else:
            Baru.Next = self.Top 
            self.Top.Prev = Baru

        self.Top = Baru
    #method hapus satu data dari stack (hapus depan)--> Pop
    def PopBrg(self, BrgKeluar):
        Phapus = self.Top
        if self.Kosong():
            print('Stack Barang Kosong')
        else:
            BrgKeluar.KodeBrg = Phapus.Brg.KodeBrg
            BrgKeluar.NamaBrg = Phapus.Brg.NamaBrg
            BrgKeluar.Stok = Phapus.Brg.Stok
            BrgKeluar.Status = Phapus.Brg.Status

            if self.SatuSimpul():
                self.Top = None
            else:
                self.Top = Phapus.Next
                self.Top.Prev = None

            del Phapus
    #method tampilkan isi stack barang
    def TampilStackBrg(self,N):
        print ('      <<-- ISI STACK BARANG (INISIALISASI)-->>')
        if (self.Kosong()):
            print('Tidak ada data barang')
        else:
            print('-------------------------------------------------------')
            print('| No | Kode Barang | Nama Barang | Stok |   Status   | ')
            print('-------------------------------------------------------')
            Bantu = self.Top
            i = N
            while (Bantu is not None):
                print(f'| {i:2} | {Bantu.Brg.KodeBrg:11} | {Bantu.Brg.NamaBrg:11} | {Bantu.Brg.Stok:4} | {Bantu.Brg.Status:10} | ')
                Bantu = Bantu.Next
                i -= 1

            print('-------------------------------------------------------')

    #method menghapus seluruh simpul (Penghancuran)
    def Penghancuran(self):
        Phapus = self.Top
        while (Phapus is not None):
            self.Top = Phapus.Next
            if (self.Top is not None):
                self.Top.Prev = None

            del(Phapus)
            Phapus = self.Top

#badan program utama
ListBrg = ListBarang()

#menambah data barang ke dalam list stack
KodeMasuk = '/'
NamaMasuk = '/'
StokMasuk = 0
StatusMasuk = '/'
BrgMasuk = DataBarang(KodeMasuk,NamaMasuk,StokMasuk,StatusMasuk)
Lagi = 'Y'
N = 0
while (Lagi != 'T'):
    os.system('cls')
    N += 1
    print('<< PENAMBAHAN DATA BARANG >>')
    BrgMasuk.KodeMasuk = str(input('Kode Barang : '))
    BrgMasuk.NamaMasuk = str(input('Nama Barang : '))
    BrgMasuk.StokMasuk = int(input('Stok        : '))
    BrgMasuk.StatusMasuk = ListBrg.StatusStok(BrgMasuk.StokMasuk)
    ListBrg.PushBrg(BrgMasuk)
    os.system('cls')
    ListBrg.TampilStackBrg(N)
    print()
    Lagi = str(input(' Mau Tambah Data Lagi[Y/T]? ')).upper()

ListBrg.Penghancuran()
os.system('cls')
ListBrg.TampilStackBrg(N)