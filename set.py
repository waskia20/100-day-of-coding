  
#set
#note:
#Tidak terurut dan tidk punya index
#Bersifat unik/ tidak bisa duplikat
#Tidak bisa diubah
#Set dibuat dengan kurung kurawal dan stiap elemen dipisah dengan koma

t = {"a",1,"b",1,"a","d","e"}
print(t)

t.add("c") #tambah elemen c
print(t) #output {1,'c','d','b','a','e'}

t.remove("a") #hapus elemen a
print(t) #{1,'c','e','d','b'}

t.discard("b") #hapus elemem b
print(t) #{1,'c','e','d'}

t.pop() #hapus elemen terakhir
print(t) #{e,'c','d'}

t.clear() #hapus semua element

