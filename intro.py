# #Ini String
# # #  nama = 'Andi'
# # # print(nama)
# # # print(type(nama))

# # # usia = 22
# # # usia = 33.0
# # # print(usia)
# # # print(type(usia))

# # # jomblo = 1
# # # jomblo = '0'
# # # print(jomblo)
# # # print(type(jomblo))
                                                                    
# # nama = int(input('Nama kamu?: ')) 
# # umur = input('Umur kamu?: ')
# # int(umur)
# # # kelamin = input('Kelamin kamu?: ')
# # # pekerjaan = input('Pekerjaan kamu?: ')

# # str()

# # int()

# # float()

# # print(nama)
# # print(type(nama))
# # print(umur)
# # print(type(umur))
# # # print(umur)
# # # print(type(umur))
# # # print(kelamin)
# # # print(type(kelamin))
# # # print(pekerjaan)
# # # print(type(pekerjaan))
# # # # print(status)

# usiaAndi =40
# usiaBudi = 15

# usiaAndi += 3
# usiaBudi *=4

# print(usiaAndi)
# print(usiaBudi)
# import math
# # print(math.pi)
# # print(math.fabs(-4.7))
# # print(math.pow(8,2))
# # print(math.sqrt(144))

# print(round(4.51))
# print(round(4.4))
# print(math.floor(4.7))
# print(math.ceil(4.4))

# x = 'Halo Dunia'

# print(len(x))
# print(x.index('a'))
# print(x.split('a'))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())

# text = "I'm Baron Nice to meet you"
# print(text[1])
# print(text[2:])
# print(text[:5])
# print(text[2:5])
# print(text[:])

# print(text[-8:-6])
# word = 'hello the world'
# # print(word[-1])
# # print(word[-5:])


# print(word.rfind('l', 0, 10))

# word = 'My name is Cornellius and Cornellius teach the data science class'
# print(word.replace('Cornellius', 'Yudha'))

# print('Cornel' + str(1))





# No1
# x=4
# y=3
# z=2
# w = ((x+y*z)/(x*y))**z
# print(w)


# #No2
# angka = int(input("Silahkan masukkan angka berapapun: "))
# print("Kuadrat dari "+ str(angka) + " = " + str(angka**2))

# No3 (total hari dijadikan satu - satu ke tahun, bulan, etc.)
# import math
# total_hari1 = int(input("masukkan hari: "))
# tahun1 = str(math.floor(total_hari1/360))
# bulan1 = str(math.floor((total_hari1 % 360)/30))
# minggu1 = str(math.floor(((total_hari1 % 360)%30)/7))
# hari1 = str(math.floor(((total_hari1 % 360)%30)%7))
# print(tahun1 + " tahun " + bulan1 + " bulan " +  minggu1 + " minggu " + hari1 + " hari ")


# #No4
# total = int(input('Total umur Andi dan Budi?: '))
# rasio = float(input('Rasio umur Andi dan Budi?: '))


# umur_budi = (total * 10) /(10 + (rasio * 10))
# umur_andi = total - umur_budi
# print('Umur Andi {}'.format(umur_andi + 2))
# print('Umur Budi {}'.format(umur_budi + 2))

# No5
# word = input('Kata: ')
# cari = input('Karakter yang ingin dicari: ')
# print(int(len(word.split(cari)))-1)



# No6
# import math

# jarak_dalam_km = int(input("Jarak antara kendaraan?: "))
# kecepatan_a_km_per_h = int(input("Kecepatan kendaraan a?: "))
# kecepatan_b_km_per_h = int(input("Kecepatan kendaraan b?: "))
# jam_berangkat = int(input('Jam Berangkat?: '))
# menit_berangkat = int(input('Menit Berangkat?: '))

# waktu_tabrakan_dalam_menit = (
#     jarak_dalam_km/(kecepatan_a_km_per_h + kecepatan_b_km_per_h))*60
# print(str(waktu_tabrakan_dalam_menit) + ' menit')

# jam = math.floor(waktu_tabrakan_dalam_menit/60) + jam_berangkat
# menit = (menit_berangkat + (waktu_tabrakan_dalam_menit%60)) % 60

# print('Waktu A & B bertabrakan adalah jam {}.{} WIB'.format(int(jam), int(menit)))
# #jam 10.12 WIB