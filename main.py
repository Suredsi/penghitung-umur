import argparse
from datetime import date,datetime


parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t','--tanggalLahir',required=True,help="masukan tanggal lahir anda")
args = parser.parse_args()
input_lahir = args.tanggalLahir
lahir = datetime.strptime(input_lahir.replace('-',' '),"%d %m %Y")


def checkumur(born):
    today = date.today()
    umur = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    if(umur< 30):
        print("Halo Kakak ",args.nama," saat ini sudah berumur:",umur," tahun")
    elif(umur > 30):
        print("Halo Bapak ",args.nama," saat ini sudah berumur:",umur," tahun")

checkumur(lahir)
