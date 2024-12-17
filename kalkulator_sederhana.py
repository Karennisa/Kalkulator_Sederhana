print(20*'=')
print("Kalkulator Sederhana")
print(20*'='+'\n')

angka_1 = float(input("masukkan angka pertama : "))
operator = input("masukkan operatornya (+ , -, *, /, %, ^) : ")
angka_2 = float(input("masukkan angka kedua : "))

#percabangan
if operator == "+":
    hasil = angka_1 +  angka_2
    print (f"hasilnya adalah : {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print (f"hasilnya adalah : {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka_1 * angka_2
    print (f"hasilnya adalah : {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print (f"hasilnya adalah : {hasil}")
elif operator == "%":
    hasil = (angka_1 / angka_2) * 100
    print (f"hasilnya adalah : {hasil:.2f}%")
elif operator == "^":
    hasil = angka_1 ** angka_2
    print (f"hasilnya adalah : {hasil}")
else : print ("tidak terbaca oleh sistem")


