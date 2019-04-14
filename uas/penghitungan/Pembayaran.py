def pembayaran() :
    from texttable import Texttable
    table1 = Texttable ()
    no1 = 0
    jawab = "y"

    while(jawab == 'y'):
        nama = (input("masukan nama: "))
        nim = (input("masukan nim: "))
        kelas = (input("masukan kelas: "))
        
        pilih1 = (input("bayar bulanan (y/t): "))
        if pilih1 == 'y':
            bulanan = 500000
        else :
            bulanan = 0

        pilih2 = (input("bayar uts (y/t): "))
        if pilih2 == 'y':
            uts = 50000
        else :
            uts = 0

        pilih3 = (input("bayar uas (y/t): "))
        if pilih3 == 'y':
            uas = 50000
        else :
            uas = 0

        pilih4 = (input("bayar seminar (y/t): "))
        if pilih4 == 'y':
            seminar = 100000
        else :
            seminar = 0

        pilih5 = (input("bayar kas (y/t): "))
        if pilih5 == 'y':
            kas = 20000
        else :
            kas = 0
            
        print("pembayaran admin 5000")
        admin = 5000
        total = bulanan+uts+uas+seminar+kas+admin
        no1 += 1
        
        table1.add_rows([['no','nama','nim','kelas','bulanan','uts','uas','seminar','kas','admin','total'],[no1,nama,nim,kelas,bulanan,uts,uas,seminar,kas,admin,total]])
        print (table1.draw())
    
        jawab=input("tambakan pembayaran (y/t): ")   
        
            
    
