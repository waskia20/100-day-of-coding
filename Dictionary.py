#note
#data disimpan dalam bentuk pasangan kunci-nilai (pair of key value) yang bersifat tidak berurutan
#dictionary dibuat dengan
#->menggunakan kurung kurawal
#->setiap pasangan elemen dipisah dengan koma
#->key dan value dipisah dengan titik dua

d = {"nama":"waskia","umur":20,"jk":"perempuan"}
print(d) #{'nama':'waskia','umur':20,'jk':'perempuan'}

print(d["nama"]) #waskia
print(d.get("nama")) #waskia

d["umur"] = 18
print(d) #{'nama':'waskia','umur':18,'jk':'perempuan'}

d["tinggi"] = 159
print(d)  #{'nama':'waskia','umur':18,'jk':'perempuan', 'tinggi': 159}

d.pop("jk")
print(d)  #{'nama':'waskia','umur':18, 'tinggi': 159}

d.clear()
print(d) #{}
