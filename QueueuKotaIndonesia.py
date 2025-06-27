#Program Queue Kota Indonesia
#I.S. : pengguna memilih salah satu nomor menu
#F.S. : program menampilkan data kota Indonesia sesuai pilihan pengguna

import os

#Konstanta
MAKSKOTA = 6

class Queue_Kota:
    #Method inisialisasi
    def __init__(self):
        self.Front = -1
        self.Rear  = -1
        self.QueueKota = ['_'] * MAKSKOTA #Queue Linier
        self.Front2 = -1
        self.Rear2  = -1
        self.QueueKota2 = ['_'] * MAKSKOTA #Queue Circular
        
    #Methed cek Queue kosong atau tidak (Linier)
    def Kosong(self):
        return self.Rear == -1
    
    #Methed cek Queue kosong atau tidak (Circular)
    def Kosong2(self):
        return self.Rear2 == -1
    
    #Methed cek Queue penuh atau tidak (Linear)
    def Penuh(self):
        return self.Rear == MAKSKOTA - 1
    
    #Methed cek Queue penuh atau tidak (Circular)
    def Penuh2(self):
        return (self.Front2 == 0 and self.Rear2 == MAKSKOTA - 1) or (self.Front2 == self.Rear2 + 1)
    
    #Method Enqueue Linear
    def Enqueue(self,KotaBaru):
        if (not self.Penuh()):
            if (self.Kosong()):
                self.Front = 0
                self.Rear  = 0
            else:
                self.Rear += 1
            
            self.QueueKota[self.Rear] = KotaBaru
        else:
            print('Queue Linear sudah penuh')
    
    #Method Enqueue Circular
    def Enqueue2(self,KotaBaru):
        if (not self.Penuh2()):
            if (self.Kosong2()):
                self.Front2 = 0
                self.Rear2  = 0
            else:
                if (self.Rear2 == MAKSKOTA-1):
                    self.Rear2 = 0
                else:
                    self.Rear2 += 1
            #MEMASUKKAN DATA YANG BARU KE QUEUE CIRCULAR
            self.QueueKota2[self.Rear2] = KotaBaru
        else:
            print('Queue Circular sudah penuh')
            
    #Method Dequeue Linear
    def Dequeue(self):
        if (not self.Kosong()):
            Item = self.QueueKota[self.Front]
            print(f'Kota yang keluar dari Queue : {Item}')
            if (self.Front == self.Rear):
                self.QueueKota[self.Rear] = '_'     
                self.Front = -1
                self.Rear  = -1
            else:
                for i in range(self.Rear):
                    self.QueueKota[i] = self.QueueKota[i+1]
                self.QueueKota[self.Rear] = '_'
                self.Rear -= 1
        else:
            print('Queue Linear Kosong')
    
    #Method Dequeue Linear
    def Dequeue2(self):
        if (not self.Kosong2()):
            Item = self.QueueKota2[self.Front2]
            print(f'Kota yang keluar dari Queue : {Item}')
            self.QueueKota2[self.Front2] = '_'
            if (self.Front2 == self.Rear2):
                self.Front2 = -1
                self.Rear2  = -1
            else:
                if (self.Front2 == MAKSKOTA-1):
                    self.Front2 = 0
                else:
                    self.Front2 += 1
        else:
            print('Queue Circular Kosong')
    
#Subruti Menu Utama
def MenuUtama(Pilih):
    print('<< MENU UTAMA >>')
    print('1. Tambah Data ke Queue (Enqueue)')
    print('2. Keluar Data dari Queue (Dequeue)')
    print('0. Keluar Menu Utama')
    Pilih= int(input('Pilihan Anda? '))
    
    return Pilih
#Subrutin menampilkan isi Queue
def TampilData(Front,Rear,QueueKota,Keterangan):
    print('<< ISI QUEUE ',Keterangan,' >>')
    print(f'Front = {Front + 1}, Rear = {Rear + 1}')
    print('Queue : ',end='')
    for i in range(MAKSKOTA):
        print(QueueKota[i],end='')
        if (i < MAKSKOTA - 1):
            print(',',end='')
        
    print()
    
#Badan Program Utama
Queue = Queue_Kota()
os.system('cls')
TampilData(Queue.Front,Queue.Rear,Queue.QueueKota,"LINIEAR")
print()
TampilData(Queue.Front2,Queue.Rear2,Queue.QueueKota2,"CIRCULAR")

#Menampilkan menu utama
os.system('cls')
Pilih = 0
Pilih = MenuUtama(Pilih)
while (Pilih != 0):
    os.system('cls')
    match (Pilih):
        case 1 :
            KotaBaru = str(input('Masukan Nama Kota di Indonesia : ')).upper()
            os.system('cls')
            Queue.Enqueue(KotaBaru)
            TampilData(Queue.Front,Queue.Rear,Queue.QueueKota,"LINIEAR")
            print()
            Queue.Enqueue2(KotaBaru)
            TampilData(Queue.Front2,Queue.Rear2,Queue.QueueKota2,"CIRCULAR")
        case 2 :
            Queue.Dequeue()
            TampilData(Queue.Front,Queue.Rear,Queue.QueueKota,"LINIEAR")
            print()
            Queue.Dequeue2()
            TampilData(Queue.Front2,Queue.Rear2,Queue.QueueKota2,"CIRCULAR")
    
    print()
    os.system('Pause')
    os.system('cls')
    Pilih = MenuUtama(Pilih)