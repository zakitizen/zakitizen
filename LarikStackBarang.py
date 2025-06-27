#Program Array Stack Barang
#I.S.: diberikan harga barang terhadap top dan elemen stack
#F.S.: menampilkan isi stack barang
import os

#konstanta untuk maksimal elemen stack
MAKSBRG = 10

#pendefinisian array stack barang
class StackBarang:
    def __init__(self):
        self.Top = -1
        self.KodeBrg = ['/'] * MAKSBRG
        self.NamaBrg = ['/'] * MAKSBRG
        self.Status = ['/'] * MAKSBRG
        self.Stok= [0] * MAKSBRG

    #menampilkan hasil inisialisasi
    def TampilInisialisasi(self,MAKSBRG):
        print ('      <<-- ISI STACK BARANG (INISIALISASI)-->>')
        print('=======================================================')
        print('| Indeks | Kode Barang | Nama Barang | Stok | Status | ')
        print('-------------------------------------------------------')
        for i in range(MAKSBRG-1,-1,-1):
            print(f'| {i+1:6} | {self.KodeBrg[i]:11} | {self.NamaBrg[i]:11} | {self.Stok[i]:4} | {self.Status[i]:6} | ')
        print('======================================================')

    #method mengecek stack kosong atau tidak
    def Kosong(self):
        return self.Top == - 1

    #method mengecek stack penuh atau tidak
    def Penuh(self):
        return self.Top == MAKSBRG - 1
    
    #method menentukan status stok
    def StatusStok(self,Stok):
        if (Stok > 0):
            return 'Aman'
        else:
            return 'Tidak Aman'

    #method menambah satu data kedalam stack (push)
    def PushBrg(self,KodeMasuk,NamaMasuk,StokMasuk,StatusMasuk):
        if (not self.Penuh()):
            self.Top += 1
            self.KodeBrg[self.Top] = KodeMasuk
            self.NamaBrg[self.Top] = NamaMasuk
            self.Stok[self.Top] = StokMasuk
            self.Status[self.Top] = StatusMasuk
        else:
            print('Stack barang penuh')

    #method mengeluarkan satu data dari stack (pop)
    def PopBrg(self):
        if (not self.Kosong()):
            KodeKeluar = self.KodeBrg[self.Top]
            NamaKeluar = self.NamaBrg[self.Top]
            StokKeluar = self.Stok[self.Top]
            StatusKeluar = self.Status[self.Top]
            self.KodeBrg[self.Top] = '/'
            self.NamaBrg[self.Top] = '/'
            self.Stok[self.Top] = 0
            self.Status[self.Top] = '/'
            self.Top -= 1
            #menampilkan data barang yang keluar 
            os.system('cls')
            print('<<--DATA BARANG KELUAR-->>')
            print(f'Kode Barang : {KodeKeluar}')
            print(f'Nama Barang : {NamaKeluar}')
            print(f'Stok        : {StokKeluar}')
            print(f'Status      : {StatusKeluar}')
        else:
            print('Stack barang kosong')


    #method menampilkan isi stack
    def TampilStackBrg(self,N):
        print ('      <<-- ISI STACK BARANG (INISIALISASI)-->>')
        if (self.Kosong()):
            print('Tidak ada data barang')
        else:
            print(f'Posisi Top = {self.Top+1}')
            print('=======================================================')
            print('| No | Kode Barang | Nama Barang | Stok |   Status   | ')
            print('=======================================================')
            for i in range(N-1,-1,-1):
                print(f'| {i+1:2} | {self.KodeBrg[i]:11} | {self.NamaBrg[i]:11} | {self.Stok[i]:4} | {self.Status[i]:10} | ')
            print('======================================================')



#badan program utama
os.system('cls')
Brg = StackBarang()
Brg.TampilInisialisasi(MAKSBRG)
os.system('pause')

#memasukkan data barang ke dalam stack
Lagi = 'Y'
N = 0
while (Lagi != 'T') and (not Brg.Penuh()):
    os.system('cls')
    N += 1
    print('<< PENAMBAHAN DATA BARANG >>')
    KodeMasuk = str(input('Kode Barang : '))
    NamaMasuk = str(input('Nama Barang : '))
    StokMasuk = int(input('Stok        : '))
    StatusMasuk = Brg.StatusStok(StokMasuk)
    Brg.PushBrg(KodeMasuk,NamaMasuk,StokMasuk,StatusMasuk)
    os.system('cls')
    Brg.TampilStackBrg(N)
    print()
    Lagi = str(input(' Mau Tambah Data Lagi[Y/T]? ')).upper()

os.system('cls')
BrgKeluar = str(input('Mau Keluar Barang[Y/T]? ')).upper()
if (BrgKeluar == 'Y'):
    Lagi = 'Y'
    while (Lagi != "T") and (not Brg.Kosong()):
        os.system('cls')
        Brg.PopBrg()
        N -= 1
        print()
        Brg.TampilStackBrg(N)
        print()
        Lagi = str(input(' Mau Tambah Data Lagi[Y/T]? ')).upper()