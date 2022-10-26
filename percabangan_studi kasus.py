"""
tentukan Variabel:
nama pembeli,no_hp,jurusan,kota,harga,jumlah beli,potongan,total,uang bayar,uang kembali
"""

#input
namapembeli = input("Masukkan Nama Pembeli :")
no_hp = input("Masukkan Nomor Handphone :")
jurusan = input("Masukkan Jurusan [SBY/BL/LMP]:")
jumlahbeli = int(input("Masukkan Jumlah Beli:"))


#proses
#proses kondisi jurusan                       
if jurusan == "SBY" or jurusan == "sby":
  kota = "surabaya"
  harga = 300000                      
elif jurusan == "BL" or jurusan == "bl":
  kota = "Bali"
  harga = 350000
else:
 kota = "lampung"
 harga = 500000

#potongan/diskon
if jumlahbeli >= 3:
  potongan = (jumlahbeli*harga)*0,1
else:
  potongan = 0

#total
total = (jumlahbeli * harga)- potongan
#Output
print("--------------------------------")
print("    PEMBELIAN TIKET BUS")
print("          xyz")
print("--------------------------------")
print("Namapembeli                 :",namapembeli)
print("Nomor Handphone             :",no_hp)
print("kode jurusan yang dipilih   :",jurusan)
print("kota tujuan yang dipilih    :",kota)
print("harga                       :",harga)
print("jumlah beli                 :",jumlahbeli)
print("total                       :",total)
print("--------------------------------")
print("potongan yang didapat       :",potongan)
print("Total Bayar                 :",total)
uangbayar = int(input("Masukkan uang bayar :"))
uangkembali = uangbayar - total
print("Uang Kembali                :",uangkembali)
print("--------------------------------")
