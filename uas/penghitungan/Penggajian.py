def penggajian() :
    from texttable import Texttable
    table1 = Texttable ()
    no1 = 0
    nama1 = []
    jabatan = []
    gaji = []
    jawab1 = "y"

    while (jawab1 == 'y'):
        nama1.append(input("Masukan Nama: "))
        jab = input("Jabatan : ")
        jabatan.append(jab)
        if  (jab == 'programer') :
            gaji.append(3000000)
        
            jawab1 = input("\nTambah Lagi? ")
        elif (jab == 'formen') :
            gaji.append(2000000)
        
            jawab1 = input("\nTambah Lagi? ")
        elif (jab == 'leader') :
            gaji.append(1000000)
            jawab1 = input("\n tambah lagi : ")
            
        else:
            break
            jawab1 = input("\n tambah lagi : ")
            
        no1+=1
        
    for i1 in range (no1) :

        table1.add_rows([['No','Nama','Jabatan','Gaji'], [i1+1, nama1[i1],jabatan[i1],gaji[i1]]])                      
    print(table1.draw())

