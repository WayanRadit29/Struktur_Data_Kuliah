masukkan = input()

#Inisialisasi stack kosong untuk simpan kurung pembuka
def isBalance(masukkan):
    stak = []
        
        #Inisialisasi dictionary untuk simpan pasangan antar kurung
    pasangan = { 
            ')' : '(', 
            '}' : '{',
            ']' : '['
        }
        
        #Parsing setiap karakter di string
    for kurung in masukkan:
            if kurung in "({[":  #Jika kurung pembuka, tambahkan ke stack
                stak.append(kurung)
            elif kurung in ")}]":  #Jika kurung penutup
                if not stak:  #Jika stack kosong, langsung return NO
                    return 'NO'
                elif stak[-1] == pasangan[kurung]:  #Cek apakah cocok dengan elemen terakhir stack
                    stak.pop()
                else:
                    return 'NO'
                    
        
        #Jika stack kosong setelah iterasi, berarti seimbang
    if not stak:
        return 'YES'
    else:
        return 'NO'

print(isBalance(masukkan))