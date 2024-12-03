data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    }
}

# Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    for tanaman, jumlah in data['hasil_panen'].items():
        print(f"{tanaman.capitalize()}: {jumlah}")
    print()

# Tampilkan jumlah hasil panen jagung dari lokasi2
jumlah_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung dari Lokasi 2: {jumlah_jagung_lokasi2}")

# Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari Lokasi 3: {nama_lokasi3}")

# Masukkan jumlah hasil panen padi dan kedelai setiap lokasi ke dalam variabel yang berbeda
jumlah_padi = {}
jumlah_kedelai = {}
for lokasi, data in data_panen.items():
    jumlah_padi[lokasi] = data['hasil_panen']['padi']
    jumlah_kedelai[lokasi] = data['hasil_panen']['kedelai']

# Buat percabangan untuk perhatian khusus
for lokasi, data in data_panen.items():
    if data['hasil_panen']['padi'] > 1300 or data['hasil_panen']['jagung'] > 800:
        print(f"Lokasi {data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {data['nama_lokasi']} dalam kondisi baik.")
