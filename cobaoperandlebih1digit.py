import os

#konstanta maksimal elemen simbol infix 
MAKSSIMBOL = 30

#membuat kelas untuk infix menjadi postfix
class InfixPostfix:
    #method inisialisasi 
    def __init__(self):
        self.Top = -1
        self.Q = ['']*MAKSSIMBOL #penampung notasi infix
        self.P = ['']*MAKSSIMBOL #penampung notasi postfix
        self.Stack = ['']*MAKSSIMBOL
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
        self.Stack[self.Top] = ''
        self.Top -= 1

    #method mengubah infix menjadi postfix
    def UbahPostfix(self,N):
        self.Push('(')
        self.Q[N] = ')'

        i = 0
        j = 0
        while(not self.Kosong()):
            if (self.Q[i] not in self.Operator) and (self.Q[i] != '(') and (self.Q[i] != ')'):
                self.P[j] = self.Q[i]
                j += 1
            elif (self.Q[i] == '('):
                self.Push('(')
            elif (self.Q[i] in self.Operator):
                while self.Stack[self.Top] in self.Operator and self.TingkatOperator(self.Stack[self.Top]) >= self.TingkatOperator(self.Q[i]):
                    self.P[j] = self.Stack[self.Top]
                    j += 1
                    self.Pop()
                self.Push(self.Q[i])
            elif (self.Q[i] == ')'):
                while (self.Stack[self.Top] != '('):
                    self.P[j] = self.Stack[self.Top]
                    j += 1
                    self.Pop()
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
        self.P[N] = ')'
        j = 0
        while self.P[j] != ')':
            if(self.P[j] not in self.Operator):
                self.Push(self.P[j])
            else:
                A = int(self.Stack[self.Top])
                self.Pop()
                B = int(self.Stack[self.Top])
                self.Pop()

                match self.P[j]:
                    case '+': Hitung = B + A
                    case '-': Hitung = B - A
                    case '*': Hitung = B * A
                    case '/': Hitung = B / A
                    case '^': Hitung = B ** A

                self.Push(str(Hitung))  # simpan sebagai string untuk konsistensi
            j += 1
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


N = len(E)
print('Q = ', end='')
j = 0
temp = ''
#tokenisasi operand agar bisa lebih dari 1 digit
for i in range(N):
    if E[i].isdigit():
        temp += E[i]
    else:
        if temp:
            Notasi.Q[j] = temp
            print(Notasi.Q[j], end=' ')
            j += 1
            temp = ''
        if E[i] != ' ':
            Notasi.Q[j] = E[i]
            print(Notasi.Q[j], end=' ')
            j += 1
if temp:
    Notasi.Q[j] = temp
    print(Notasi.Q[j], end=' ')
    j += 1

N = j
print()
N = Notasi.UbahPostfix(N)
Notasi.TampilPostfix(N)

#memanggil hasil perhitungan postfix 
print()
Notasi.HitungPostfix(N)
