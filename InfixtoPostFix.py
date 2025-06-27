#program mengubah infix menjadi postfix
#I.S : pengguna memasukkan sebuah ekspresi infix (E)
#F.S : menampilkan hasil postfix dan hasil perhitungan nya
import os

#konstanta maksimal elemen simbol infix 
MAKSSIMBOL = 30

#membuat kelas untuk infix menjadi postfix
class InfixPostfix:
    #method inisialisasi 
    def __init__(self):
        self.Top = -1
        self.Q = [' ']*MAKSSIMBOL #penampung notasi infix
        self.P = [' ']*MAKSSIMBOL #penampung notasi postfix
        self.Stack = [' ']*MAKSSIMBOL
        self.Operator = set(['+','-','*','/','^'])

    #method mengecek stack kosong atau tidak
    def Kosong(self):
        return self.Top == -1
    
    #method menentukan tingkatan operator
    def TingkatOperator(self,Opr):
        if (Opr == '+') or (Opr == '-'):
            return 1
        elif (Opr == '*') or (Opr == '/'):
            return 2
        else:
            return 3
        
    #method memasukkan satu simbol ke stack (push)
    def Push(self,Simbol):
        self.Top += 1
        self.Stack[self.Top] = Simbol

    #method mengeluarkan satu elemen dari stack (pop)
    def Pop(self):
        self.Stack[self.Top] = ' '
        self.Top -= 1

    #method mengubah infix menjadi postfix
    def UbahPostfix(self,N):
        #push kurung buka
        self.Push('(')
        #tambahkan kurung tutup di sentinel Q
        self.Q[N] = ')'

        #pindai simbol Q dari kiri ke kanan sampai stack kosong
        i = 0 #indeks array Q
        j = 0 #indeks array P
        while(not self.Kosong()):
            #jika yang dipindai operand
            if (self.Q[i] not in self.Operator)and(self.Q[i] != '(') and(self.Q[i] != ')'):
                #tambahkan ke p
                self.P[j] = self.Q[i]
                j += 1
            elif (self.Q[i] == '('): #jika yang dipindai kurung
                #push ke stack
                self.Push('(')
            elif (self.Q[i] in self.Operator): #jika yang dipindai operator
                #cek isi teratas stack
                while self.Stack[self.Top] in self.Operator and self.TingkatOperator(self.Stack[self.Top]) >= self.TingkatOperator(self.Q[i]):
                    #pop , tambahkan ke P 
                    self.P[j] = self.Stack[self.Top]
                    j += 1
                    self.Pop()

                #push simbol yang di pindai ke stack
                self.Push(self.Q[i])
            elif (self.Q[i] == ')'): #jika yang dipindai kurung tutup
                #pop sampai ketemu kurung buka
                while (self.Stack[self.Top] != '('):
                    #pop lalu tambahkan ke p
                    self.P[j] = self.Stack[self.Top]
                    j += 1
                    self.Pop()
                
                #pop kurung buka
                self.Pop()

            i += 1

        return j

    #method menampilkan hasil postfix
    def TampilPostfix(self,N):
        print('P = ',end='')
        for j in range(N):
            print(self.P[j],end='')
            if (j < N-1):
                print(', ',end='')

    #method menghitung dalam keadaan postfix
    def HitungPostfix(self,N):
        #tambahkan kurung tutup di sentinel P
        self.P[N] = ')'

        #pindai simbol di P dari kiri ke kanan sampai kurung tutup
        j = 0
        while self.P[j] != ')':
            #jika di pindai operand
            if(self.P[j] not in self.Operator):
                #push ke stack
                self.Push(self.P[j])
            else: #jika yang dipindai operator 
                #pop dua elemen teratas stack
                A =  int(self.Stack[self.Top])
                self.Pop()
                B =  int(self.Stack[self.Top])
                self.Pop()

                #hitung dengan rumus B operator A
                match self.P[j]:
                    case '+': Hitung = B + A
                    case '-': Hitung = B - A
                    case '*': Hitung = B * A
                    case '/': Hitung = B / A
                    case '^': Hitung = B ** A

                #push hasil perhitungan 
                self.Push(Hitung)

            j += 1
        #pop isi stack, simpan di var.value
        Value = self.Stack[self.Top]
        self.Pop()
        print(f'Value = {Value}')
#badan program utama
Notasi = InfixPostfix()

#memasukkan sebuah ekspresi infix (E)
os.system('cls')
print('<< PROGRAM MENGUBAH INFIX MENJADI POSTFIX >>')
print('--------------------------------------------')
E = str(input('Notasi Infix (E) = '))
#validasi simbol di E tidak bole leboh dari MAKSSIMBOL

#memasukkan ekspresi infix ke notasi Q
N = len(E)
print('Q = ',end='')
j = 0
for i in range(N):
    #validasi melewati spasi di E
    if (E[i] != ' '):
        Notasi.Q[j] = E[i]
        print(Notasi.Q[j],end=' ')
        j += 1

#validasi agar operand bisa lebih dari 1 digit



N = j
print()
N = Notasi.UbahPostfix(N)
Notasi.TampilPostfix(N)

#memanggil hasil perhitungan postfix 
print()
Notasi.HitungPostfix(N)