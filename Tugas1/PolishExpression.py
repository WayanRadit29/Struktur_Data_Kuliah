#Membuat Fungsi untuk menentukan prioritas operator
def priority(operator):
    if operator in ('+','-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    elif operator == '^':
        return 3

#Simpan semua hasil akhir di list 
all_results = []


t = int(input())

for _ in range(t):
    expression = input()
    stack = []
    storage = ""  #Untuk penyimpanan hasil sementara

    for i in expression:
        if i.isalpha() and i.islower():
            storage += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                storage += stack.pop()
            if stack:
                stack.pop()  #Pop tanda '('
        elif i in "+-*/^":
            while stack and stack[-1] in "+-*/^":
                if priority(i) < priority(stack[-1]):
                    storage += stack.pop()
                else:
                    break
            stack.append(i)

    #Setelah loop selesai, pop sisa operator di stack
    while stack:
        storage += stack.pop()

    #Tambahkan hasil ke 'all_results'
    all_results.append(storage)

    #Bersihkan stack (opsional, karena loop akan membuat stack baru)
    stack.clear()

#Setelah semua test case selesai, cetak hasilnya sekaligus
for res in all_results:
    print(res)
