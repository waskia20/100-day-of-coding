#studi kasus
#lakukan perulangan input data sebanyak 5 kali dengan data dibawah ini:
#Data ke- <berulang>
#Masukkan NIM anda:<Input Data ke 1>
#Masukkan Nilai UTS:<Input Data ke 1>
#Masukkan Nilai UAS:<Input Data ke 1>

#Output
#Nim anda adalah <outputnim1> nilai UTS anda <outpututs1>nilai UTS anda<outputuas1>

ulang = 5
#i = 0
for i in range(ulang):
    print("data ke - " + str(i+1))
    nama = input("Masukkan Nama anda:")
    uts =int(input("Masukkan Nilai UTS anda:"))
    uas =int(input("Masukkan Nilai UAS anda:"))
    print("Nama anda adalah %s nilai UTS anda %i nilai UAS anda %i" % (nama,uts,uas))
    print("-----------------------------------------")
