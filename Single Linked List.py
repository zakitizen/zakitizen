# Program Single Linked List
# I.S.: diberikan harga awal terhadap pointer kepala (Awal)
# F.S.: menampilkan isi List
import os

# Pendefinisian linked list
# 1. Membuat kelas untuk simpul
class Node:
    def __init__(self, Info):
        self.Info = Info
        self.Next = None

# 2. Membuat kelas untuk linked list
class SingleLinkedList:
    def __init__(self):
        self.Awal = None

    # Method memeriksa list kosong atau tidak
    def Kosong(self):
        return self.Awal is None  # True jika kosong, False jika tidak kosong

    # Method untuk menampilkan isi linked list
    def TampilData(self):
        print("<<Isi Linked List>>")
        if self.Kosong():
            print("Linked List Kosong")
        else:
            Bantu = self.Awal
            while Bantu is not None:
                print(Bantu.Info, end=" ")
                if Bantu.Next is not None:
                    print("-->", end=" ")
                Bantu = Bantu.Next
            print("\nIsi Linked List:")
        print()

    # Method untuk menghancurkan/menghapus simpul yang ada di linked list
    def Penghancuran(self):
        Phapus = self.Awal
        while Phapus is not None:
            self.Awal = Phapus.Next
            del Phapus
            Phapus = self.Awal

    # Method menu penambahan data
    def MenuTambah(self, Pilih):
        os.system('cls')
        print("<<Menu Penambahan Data>>")
        print("1. Tambah di Depan")
        print("2. Tambah di Belakang")
        print("3. Tambah di Tengah")
        print("0. Keluar Menu Tambah Data")
        Pilih = int(input("Pilihan anda? "))
        return Pilih

    # Method menambah satu simpul di depan
    def SisipDepanSingle(self, AngkaBaru):
        Baru = Node(AngkaBaru)
        if self.Kosong():
            Baru.Next = None
        else:
            Baru.Next = self.Awal
        self.Awal = Baru

    # Method menambah satu simpul di belakang
    def SisipBelakangSingle(self, AngkaBaru):
        Baru = Node(AngkaBaru)
        if self.Kosong():
            self.Awal = Baru
        else:
            Bantu = self.Awal
            while Bantu.Next is not None:
                Bantu = Bantu.Next
            Bantu.Next = Baru

    # Method menambah satu simpul di tengah
    def SisipTengahSingle(self, AngkaBaru):
        SisipSetelah = int(input(f"Angka {AngkaBaru} akan disisipkan setelah angka: "))
        Bantu = self.Awal
        Ketemu = False
        while not Ketemu and Bantu is not None:
            if Bantu.Info == SisipSetelah:
                Ketemu = True
            else:
                Bantu = Bantu.Next
        if Ketemu:
            Baru = Node(AngkaBaru)
            Baru.Next = Bantu.Next
            Bantu.Next = Baru
        else:
            print(f"Angka {SisipSetelah} tidak ditemukan!")

#method menyusun  secara ascending
def UrutNIMAsc(self):
    if self.Kosong():
        print('List masih kosong')
    else:
        i = self.Awal
        while i is not None:
            j = self.Awal
            while j.Next is not None:
                if j.Info > j.Next.Info:
                    # pertukaran data
                    Temp = j.Info
                    j.Info = j.Next.Info
                    j.Next.Info = Temp
                j = j.Next
            i = i.Next

#method menyusun  secara descending
def UrutNIMAsc(self):
    if self.Kosong():
        print('List masih kosong')
    else:
        i = self.Awal
        while i is not None:
            j = self.Awal
            while j.Next is not None:
                if j.Info < j.Next.Info:
                    # pertukaran data
                    Temp = j.Info
                    j.Info = j.Next.Info
                    j.Next.Info = Temp
                j = j.Next
            i = i.Next

# Inisialisasi linked list
List1 = SingleLinkedList()

# Membuat dua buah simpul (Node1 dan Node2)
Node1 = Node(5)
Node2 = Node(3)

# Menyambungkan simpul yang ditunjuk Node1 dengan simpul yang ditunjuk Node2
Node1.Next = Node2
Node2.Next = None

# Menjadikan linked list
List1.Awal = Node1

# Memanggil method menampilkan isi list
os.system('cls')
List1.TampilData()
print()
os.system('pause')

# Menambahkan simpul baru dengan angka 99 di akhir
List1.SisipBelakangSingle(99)

os.system('cls')
List1.TampilData()
print()
os.system('pause')

# Membuat satu simpul lagi, medan data diisi angka 100, lalu ditambahkan di depan
List1.SisipDepanSingle(100)

List1.TampilData()
print()
os.system('pause')

Pilih = List1.MenuTambah(0)
while Pilih != 0:
    os.system('cls')
    match Pilih:
        case 1:
            print("<<Tambah di Depan>>")
            AngkaBaru = int(input("Masukkan sebuah angka: "))
            List1.SisipDepanSingle(AngkaBaru)
            print()
            List1.TampilData()
        case 2:
            print("<<Tambah di Belakang>>")
            AngkaBaru = int(input("Masukkan sebuah angka: "))
            List1.SisipBelakangSingle(AngkaBaru)
            print()
            List1.TampilData()
        case 3:
            print("<<Tambah di Tengah>>")
            if List1.Kosong():
                print("Linked List Kosong")
            else:
                AngkaBaru = int(input("Masukkan sebuah angka: "))
                List1.SisipTengahSingle(AngkaBaru)
                print()
                List1.TampilData()
    os.system('pause')
    Pilih = List1.MenuTambah(Pilih)
# ...existing code...
os.system('cls')
print('DATA SEBELUM TERURUT')
List1.TampilData()
print()
print('DATA SETELAH TERURUT ASCENDING')
List1.UrutAsc()
List1.TampilData()
os.system('pause')
print('DATA SEBELUM TERURUT')
List1.TampilData()
print('DATA SETELAH TERURUT DESCENDING')
List1.UrutNIMDesc()
List1.TampilData()
# ...existing code...
# Memanggil method penghancuran
List1.Penghancuran()
print()
List1.TampilData()






