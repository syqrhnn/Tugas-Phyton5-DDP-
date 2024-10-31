#Jawaban NO.1
#Buat variabel list dengan value : [namaKendaraan, JenisKendaraan, ccKendaraan, warna kendaraan, roda kendaraan]
kendaraan = ['Astrea', 'Sepeda Motor', 160, 'Biru', 2]
print("kendaraan saya")
print(kendaraan)
print("=======")
#tambahkan dari list tersebut di belakang dengan value : [harga kendaraan, tipe kendaraan]
#kendaraan.append(20000000)
#kendaraan.append('Matic')
kendaraan.extend([20000000, 'Matic'])
print(kendaraan)
print("=======")
#tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
kendaraan.insert(2, 'honda')
print(kendaraan)
print("=======")

#Jawaban NO.2
#Buat program phyton dengan match case untuk menghitung luas bangun datar :
#jika pilih 1, maka menghitung luas persegi
#jika pilih 2, maka menghitung luas lingkaran
#jika pilih 3, maka menghitung luas segitiga
#kalau pilihannya tidak ada maka ada keterangan : salah pilih

print('Ini adalah program sederhana untuk menghitung luas bangun datar')
print('Pilih menu angka 1-5 : \n1. persegi\n2. lingkaran\n3. segitiga\n4. jajar genjang\n5. trapesium')
pilihMenu = int(input('Silahkan pilih menu dengan mengetikkan angka 1-5: '))
match pilihMenu:
    case 1:
        print("Ini adalah menu untuk menghitung luas persegi")
        sisi = int(input('silakan masukan nilai yang mau dihitung: '))
        hitung = sisi * sisi
        print("Luas persegi adalah : " , hitung )
    case 2:
        print("Ini adalah menu untuk menghitung luas lingkaran")
        phi = 22/7
        r = int(input('silahkan masukkan nilai jari-jari: '))
        hitung = phi * r * r
        print("Luas lingkaran adalah : ", hitung )
    case 3:
        print("Ini adalah menu untuk menghitung luas segitiga")
        alas = int(input('silahkan masukkan nilai alas: '))
        tinggi = int(input('silahkan masukkan nilai tinggi: '))
        hitung = 1/2 * alas * tinggi
        print("Luas segitiga adalah: ", hitung)
    case 4:
        print("Ini adalah menu untuk menghitung luas jajar genjang")
        alas = int(input('silakan masukkan nilai alas: '))
        tinggi = int(input('silahkan masukkan nilai tinggi: '))
        hitung = alas * tinggi
        print("Luas Jajar Genjang adalah: ", hitung)
    case 5:
        print("Ini adalah menu untuk menghitung luas trapesium")
        sisi_a =int(input('silahkan masukkan nilai sisi a: '))
        sisi_b =int(input('silahkan masukkan nilai sisi b: '))
        tinggi =int(input('silahkan masukkan nilai tinggi: '))
        hitung = 1/2 * tinggi *(sisi_a + sisi_b)
        print("Luas trapesium adalah: ", hitung)
    case 6:
        print("Ini adalah menu untuk menghitung luas tabung")
        phi = 22/7
        jari_jari =int(input('silahkan masukkan '))
    case _:
        print("Pilihan tidak valid, silahkan pilih dari 1-5")
    