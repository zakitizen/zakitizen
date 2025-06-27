import os

#PENDEFINISIAN LINKED LIST
#1. MEMBUAT KELAS UNTUK SIMPUL
class Node:
    def __init__(self,info):
        self.info = info
        self.next = None
    
#2. MEMBUAT KELAS UNTUK LINKED LIST 
class SingleLinkedList:
    def __init__(self):
        self.awal = None
    #METHOD MEMERIKSA LIST KOSONG ATAU TIDAK
    def Kosong(self):
        kosong = False
        if self.awal is None:
            kosong = True
        return kosong
        #RETURN self.awal is None
    
     #METHOD MEMERIKSA LIST MEMILIKI SATU SIMPUL ATAU LEBIH
    def SatuNode(self):
        satunode = False
        if self.awal.next is None:
            satunode = True
        return satunode
        #RETURN self.awal.next is None

    #METHOD MENAMPILKAN SII LIST
    def TampilData(self):
        print("ISI LINKED LIST")
        if (self.Kosong()):
            print("LIST KOSONG")
        else:
            Bantu = self.awal
            while Bantu is not None:
                print(Bantu.info,end="")
                if Bantu.next is not None:
                    print(" --> ",end="")
                
                Bantu = Bantu.next
        
        print()
    
    #METHOD MENGHAPUS SEMUA SIMPUL YANG ADA DI LIST
    def Penghancuran(self):
        Phapus = self.awal
        while Phapus is not None: #while not self.kosong()
            self.awal = self.awal.next #self.awal = Phapus.next
            del(Phapus)
            Phapus = self.awal

    def MenuUtama(seld,PilihUtama):
        os.system('cls')
        print("MENU UTAMA")
        print("1. TAMBAH DATA")
        print("2. UBAH DATA")
        print("3. HAPUS DATA")
        print("4. CARI SIMPUL")
        print("3. HAPUS DATA")
        print("0. KELUAR MENU TAMBAH DATA")
        PilihUtama = int(input("Masukkan pilihan anda :"))
        return PilihUtama

    #METHOD MENU PENAMBAHAN DATA
    def Menutambah(self,pilih):
        os.system('cls')
        print("MENU TAMBAH DATA")
        print("1. TAMBAH DATA DIDEPAN")
        print("2. TAMBAH DATA DIBELAKANG")
        print("3. TAMBAH DATA DITENGAH")
        print("0. KELUAR MENU TAMBAH DATA")
        pilih = int(input("Masukkan pilihan anda :"))
        return pilih
    
    #METHOD MENAMBAH SATU SIMPUL DIDEPAN
    def SisipDepanSingle(self,AngkaBaru):
        Baru = Node(AngkaBaru)
        if self.Kosong():
            Baru.next = None
        else:
            Baru.next = self.awal
        
        self.awal = Baru

    #METHOD MENAMBAH SATU SIMPUL BELAKANG
    def SisipBelakangSingle(self,AngkaBaru):
        Baru = Node(AngkaBaru)
        if self.Kosong():
            Baru.next = None
        else:
            Bantu = self.awal
            while Bantu.next is not None:
                Bantu = Bantu.next
        
            Bantu.next = Baru

    #METHOD MENAMBAH SATU SIMPUL BELAKANG
    def SisipTengahSingle(self,AngkaBaru):
        SisipSetelah = int(input("Angka {} akan disisipkan setelah angka :".format(AngkaBaru)))
        Bantu = self.awal
        ketemu = False
        while not ketemu and Bantu is not None:
            if Bantu.info == SisipSetelah:
                ketemu = True
            else:
                Bantu = Bantu.next

        if ketemu:
            if Bantu.next is None:
                self.SisipBelakangSingle(AngkaBaru)
            else:
                Baru = Node(AngkaBaru)
                Baru.next = Bantu.next
                Bantu.next = Baru
                
        else:
            print(f"Angka {SisipSetelah} tidak ditemukan")

    #METHOD UBAH DATA
    def UbahData(self,AngkaBaru):
        if (self.Kosong()):
            print('List masih kosong, pilih menu no 1 terlebih dahulu')
        else:
            AngkaUbah = int(input('Angka yang akan diubah :'))
            bantu = self.awal
            Ketemu = False
            while not Ketemu and bantu is not None:
                if (bantu.info == AngkaUbah):
                    Ketemu = True
                else:
                    bantu = bantu.next

     #METHOD MENU PENAMBAHAN DATA
    def MenuHapus(self,PilihHapus):
        os.system('cls')
        print("MENU TAMBAH DATA")
        print("1. HAPUS DATA DIDEPAN")
        print("2. HAPUS DATA DIBELAKANG")
        print("3. HAPUS DATA DITENGAH")
        print("0. KELUAR MENU HAPUS DATA")
        PilihHapus = int(input("Masukkan pilihan anda :"))
        return PilihHapus
    
    #METHOD HAPUS DEPAN
    def HapusDepanSingle(self):
        if (self.Kosong()):
            print('Data kosong')
        else:
            Phapus = self.awal
            AngkaHapus = Phapus.info
            if (self.SatuNode):
                self.awal = None
            else:
                self.awal = Phapus.next
            
            del(Phapus)
            os.system('cls')
            print(f"Angka yang sudah dihapus adalah angka {AngkaHapus}")
    
    #METHOD HAPUS BELAKANG
    def HapusBelakangSingle(self):
        if (self.Kosong()):
            print('Data kosong')
        else:
            Phapus = self.awal
            if (self.SatuNode):
                self.awal = None
            else:
                while Phapus.next != None:
                    Phapus = Phapus.next
                bantu = self.awal
                while bantu.next != Phapus:
                    bantu = bantu.next
                bantu.next = None
            AngkaHapus = Phapus.info
            del(Phapus)
            os.system('cls')
            print(f"Angka yang sudah dihapus adalah angka {AngkaHapus}")

#BADAN PROGRAM UTAMA
#INISIALISASI LINKED LIST 
List1 = SingleLinkedList()

#MEMANGGIL METHOD MENU UTAMA
PilihUtama = 0
PilihUtama = List1.MenuUtama(PilihUtama)
while (PilihUtama != 0):
    os.system('cls')
    if PilihUtama == 1:
        pilih = 0
        pilih = List1.Menutambah(pilih)
        while pilih != 0:
            os.system('cls')
            if pilih == 1:
                print("PENAMBAHAN DATA DIDEPAN")
                AngkaBaru = int(input("Masukkan angka baru :"))
                List1.SisipDepanSingle(AngkaBaru)
                print()
                List1.TampilData()
            elif pilih == 2:
                print("PENAMBAHAN DATA DIBELAKANG")
                AngkaBaru = int(input("Masukkan angka baru :"))
                List1.SisipBelakangSingle(AngkaBaru)
                print()
                List1.TampilData()
            else:
                print("PENAMBAHAN DATA DIDEPAN")
                if List1.Kosong():
                    print("Angka masih kosong")
                else:
                    AngkaBaru = int(input("Masukkan angka baru :"))
                    List1.SisipTengahSingle(AngkaBaru)
                    print()
                    List1.TampilData()

            print()
            os.system('pause')
            pilih = List1.Menutambah(pilih)
    elif PilihUtama == 2:
        print('PENGUBAHAN DATA')
        AngkaBaru = int(input("Angka yang baru :"))
        List1.UbahData(AngkaBaru)
        print()
        List1.TampilData()
        print()
        os.system('pause')
    elif PilihUtama == 3:
       PilihHapus = 0
       PilihHapus = List1.MenuHapus(PilihHapus)
       while PilihHapus != 0:
            os.system('cls')
            match (PilihHapus):
                case 1:
                    print('PENGHAPUSAN DATA DIDEPAN')
                    List1.HapusDepanSingle()
                    print()
                    List1.TampilData()
                    print()
                    os.system('pause')
                
                case 2:
                     print('PENGHAPUSAN DATA DIBELAKANG')
                     List1.HapusBelakangSingle()
                     print()
                     List1.TampilData()
                     print()
                     os.system('pause')
                case 3:
                    print('PENGHAPUSAN DATA DITENGAH')
                    print()
                    List1.TampilData()
                    print()
                    os.system('pause')
                    PilihHapus = List1.MenuHapus(PilihHapus)
    elif PilihUtama == 4:
        print('PENCARIAN SIMPUL')
        print()
        List1.TampilData()
        print()
        os.system('pause')
    elif PilihUtama == 5:
        print('PENGURUTAN DATA')
        print()
        List1.TampilData()
        print()
        os.system('pause')
    else:
        print('Tidak Tersedia')
    PilihUtama = List1.MenuUtama(PilihUtama)
    
#MEMANGGI METHOD PENGHANCURAN
List1.Penghancuran()
print()
List1.TampilData()





