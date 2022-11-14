#Manipulasi dan Operator String

#1. Menyambung 2 buah string
string1 = "Was"
string2 = "kia"
print ("string1 : ",string1)
print ("string2 : ",string2)

string_lengkap = string1 + " " + string2
print("String Gabungan = ", string_lengkap)

# 2. Menampilkan Panjang String

nama = "Waskia" #<- Spasi Dihitung sebagai string
panjang_string = len(nama)

print(nama,"\nMemiliki Panjang :",panjang_string)

# 3. Mengecek kata dalam string
nama = "Waskia"
cek1 = "Was" 
cek2 = "kia" 
status1 = cek1 in nama  #<- Dalam Pengecekan Huruf kapital sangat berpengaruh
status2 = cek2 in nama
print ("kata",cek1,"Ada di : ",nama,"=",str(status1))
print ("kata",cek2,"Ada di : ",nama,"=",str(status2))

# 4. Mengulang String
print("he"*5)
print(5*"wk")

# 5. Index String
nama = "Waskia"
print(nama)
print ("Index String ke 0 :", nama[0])
print ("Index String ke 3 :", nama[3])
print ("Index String ke : -1", nama[-1]) #<- Mengambil String Dari Belakang
print ("Index String 0 sampai 4",nama[0:4]) #<- Yang di ambil 0 sampai sebelum 4
print ("Index String ke [0,2,4,] :", nama[0:10:2])#<- 2 disini maksudnya di lompatin 2

# 6. Mengecek Jumlah Huruf
nama = "Waskia"
jumlah_huruf = nama.count('a')
print("Jumlah 'a' dalam :",nama," = ",jumlah_huruf) #<-Huruf Kapital berpengearuh dalah pengecekan
