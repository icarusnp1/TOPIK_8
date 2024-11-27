#No 4. Skenario konflik 
data_panen = {    
    'lokasi1':{
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi':1200,
            'jagung':800,
            'kedelai':500
        }
    },
    'lokasi2':{
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi':1500,
            'jagung':900,
            'kedelai':450
        }
    },
    'lokasi3':{
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi':1100,
            'jagung':750,
            'kedelai':600
        }
    },
    'lokasi4':{
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi':1300,
            'jagung':850,
            'kedelai':550
        }
    },
    'lokasi5':{
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi':1400,
            'jagung':950,
            'kedelai':480
        }
    }
}

#1. Menampilkan seluruh data lokasi
print("--DATA LOKASI--")
print(data_panen)

#2. Jumlah hasil panen
n=1
print("--HASIL PANEN-")
for i,j in data_panen.items():
    print(f'Hasil panen lokasi ke-{n}', j['hasil_panen'])
    n+=1

#3. Lokasi ke 3
print('--NAMA LOKASI 3--')
print(data_panen['lokasi3']['nama_lokasi'])

#4. Buat variabel PADI dan KEDELAI
print('--JUMLAH HASIL PADI DAN KEDELAI--')
padi = 0
kedelai = 0

#5. Masukan jumlah hasil panen PADI dan KEDELAI
for i,j in data_panen.items():
    padi    = data_panen[i]['hasil_panen']['padi'] + padi
    kedelai   = data_panen[i]['hasil_panen']['kedelai'] + kedelai
    jagung   = data_panen[i]['hasil_panen']['jagung'] + jagung
    
print(f'PADI = {padi}')
print(f'PADI = {kedelai}')

#6. Percabangan jumlah panen PADI lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi maka perlu perhatian khusus,
# jika tidak dalam kondisi baik.
if padi > 1300:
    print("Perlu perhatian khusus")
elif jagung > 800:
    print("Kondisi baik")