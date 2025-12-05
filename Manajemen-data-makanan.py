def tampilkan_resep(nama, alat, bahan, langkah):
    print("\n" + "=" * 50)
    print("RESEP", nama.upper())
    print("=" * 50)

    print("\nALAT YANG DIPAKAI:")
    for i, item in enumerate(alat, 1):
        print(f"{i}. {item}")

    print("\nBAHAN-BAHANNYA:")
    for i, item in enumerate(bahan, 1):
        print(f"{i}. {item}")

    print("\nLANGKAH MASAK:")
    for i, item in enumerate(langkah, 1):
        print(f"{i}. {item}")

    print("=" * 50)

def resep_makanan():
    data = {}

    data["1"] = {
        "nama": "Mie Goreng",
        "alat": ["Wajan", "Spatula", "Piring", "Pisau", "Telenan"],
        "bahan": [
            "1 bungkus mie",
            "Bawang putih",
            "Bawang merah",
            "1 telur",
            "Kecap manis",
            "Kecap asin",
            "Sayuran",
            "Garam, merica",
            "Minyak"
        ],
        "langkah": [
            "Rebus mie dulu",
            "Tumis bawang sampai wangi",
            "Masukkan telur lalu orak arik",
            "Masukkan sayuran",
            "Masukkan mie + bumbu",
            "Aduk sampai rata",
            "Angkat dan sajikan"
        ]
    }

    data["2"] = {
        "nama": "Nasi Goreng",
        "alat": ["Wajan", "Spatula", "Piring", "Pisau", "Telenan"],
        "bahan": [
            "Nasi putih",
            "Bawang putih",
            "Bawang merah",
            "Telur",
            "Kecap",
            "Cabai",
            "Daun bawang",
            "Garam dan penyedap"
        ],
        "langkah": [
            "Haluskan bawang + cabai",
            "Tumis sampai harum",
            "Masukkan telur dan orak arik",
            "Masukkan nasi",
            "Kasih kecap + garam",
            "Aduk sampai rata",
            "Tambah daun bawang",
            "Sajikan"
        ]
    }

    data["3"] = {
        "nama": "Ayam Goreng",
        "alat": ["Wajan", "Piring", "Pisau", "Mangkuk", "Sendok"],
        "bahan": [
            "Ayam potong",
            "Bawang putih",
            "Kunyit",
            "Jahe",
            "Ketumbar",
            "Garam",
            "Air",
            "Minyak"
        ],
        "langkah": [
            "Haluskan bumbu",
            "Lumuri ayam dan diamkan",
            "Rebus sebentar biar bumbu masuk",
            "Panaskan minyak",
            "Goreng ayam sampai coklat",
            "Sajikan"
        ]
    }

    return data