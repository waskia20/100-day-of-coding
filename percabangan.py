#kondisi if
hari = "Minggu"

if hari == "senin":
    print("Hari ini mata kuliah pemprograman python")

#kondisi if..else
hari = "Minggu"

if hari =="senin" or hari == "selasa" or hari == "rabu" or hari == "kamis":
    print("hari ini ada perkuliahan")
else:
    print("hari ini libur tidak ada perkuliahan")

#kondisi if..elif..else
hari = "A"

if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis":
    print("Hari ini ada mata kuliah")
elif hari == "jumat" or hari == "sabtu":
    print("hari ini efektif perkuliahan tapi tidak ada mata kuliah")
elif hari == "minggu":
    print("hari libur")
else:
    print("Anda salah memasukkan hari")
    

    
