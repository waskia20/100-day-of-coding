x = [1,2,"a","a",True]
print(x)

#mendapatkan panjang list
print(len(x))#output = 5

#mengubah nilai pada index ke 1
x[1] = 3
print(x) #[1,3,"a","a",True]

#menambah element pada index terakhir
x.append(4)
print(x) #[1,3,'a','a',True,4]

#menambah elemen pada index ke 1
x.insert(1,"c")
print(x) #[1,'c',3,'a','a',True,4

#menghapus elemen c
x.remove('c')
print(x) #[1,3,'a','a',True,4]

#menghapus elemen pada index ke 0
x.pop(0)
print(x) #[3,'a','a,True,4]

x.clear()
print(x) #[]
