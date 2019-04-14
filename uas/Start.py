from penghitungan.Penggajian import penggajian
from penghitungan.Inputnilai import inputnilai
from penghitungan.Pembayaran import pembayaran
from penghitungan.Kalkulator import kalkulator
import getpass

def login () :
    print ("\nlogin")
    user = input("username : ")
    pasword = getpass.getpass("pasword : ")
    if user == 'syaifudin' and pasword == '12345':
       start ()
    else:
       login()
    
def start():
    
    print("1. gaji")
    print("2. penilaian")
    print("3. pembayaran kampus")
    print("4. kalkulator")
    pilihan = input("\nMasukan Pilihan (1/2/3/4)?  ")
    if   pilihan == '1' :
         penggajian()
    elif pilihan == '2' :
         inputnilai()
    elif pilihan == '3' :
         pembayaran()
    elif pilihan == '4' :
         kalkulator()
    else :
        print ("\n!!! Pilihan Tidak Ditemukan !!!")
    tambahan()


def tambahan() :
    
    tambah = input ("\nKembali Ke Penggajian & Nilai (y/t)? ")
    if tambah == 'y' :
        start()
    else :
        import Akhir

login()

