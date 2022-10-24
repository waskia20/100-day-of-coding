#perulangan for
#1
warna = ['Merah','Biru','Kuning','Biru']
for i in warna :
    print(i)
#2
warna = {'Merah','Biru','Kuning','Biru'}
for i in warna :
    print(i)

#3
web = 'waskia'
for huruf in web :
    print(huruf)

#4
nomor =[5,8,5,3,1,9,7,4,2]
sum = 0
for i in nomor:
    #sum = sum + i #ini bisa
    sum += i #ini juga bisa
    #print i
print("jumlah semuanya:",sum)
