
def cari_mahasiswa(data, nim):
    # Mencari mahasiswa berdasarkan NIM
    if nim in data:
        return data[nim]
    else:
        return None


def rata_rata_nilai(data):
    # Menghitung rata-rata nilai seluruh mahasiswa
    if len(data) == 0:
        return 0

    total = 0
    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# 1. Operasi pencarian mahasiswa
print("=== PENCARIAN MAHASISWA ===")
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)

if hasil is not None:
    print("NIM:", nim_cari)
    print("Nama:", hasil["nama"])
    print("Kelas:", hasil["kelas"])
    print("Nilai:", hasil["nilai"])
else:
    print("Mahasiswa tidak ditemukan.")


# 2. Operasi penambahan mahasiswa
print("\n=== PENAMBAHAN MAHASISWA ===")
nim_baru = "A006"

if nim_baru not in data_mahasiswa:
    data_mahasiswa[nim_baru] = {
        "nama": "Fani",
        "kelas": "B",
        "nilai": 90
    }
    print("Data mahasiswa berhasil ditambahkan.")
else:
    print("NIM sudah terdaftar.")

print("Data baru:", data_mahasiswa[nim_baru])


# 3. Operasi pembaruan data mahasiswa
print("\n=== PEMBARUAN DATA MAHASISWA ===")
nim_update = "A002"

if nim_update in data_mahasiswa:
    data_mahasiswa[nim_update]["nilai"] = 82
    print("Nilai mahasiswa berhasil diperbarui.")
    print("Data terbaru:", data_mahasiswa[nim_update])
else:
    print("Mahasiswa tidak ditemukan.")


# 4. Operasi rekap seluruh mahasiswa
print("\n=== REKAP DATA MAHASISWA ===")

for nim, mahasiswa in data_mahasiswa.items():
    print(
        "NIM:", nim,
        "| Nama:", mahasiswa["nama"],
        "| Kelas:", mahasiswa["kelas"],
        "| Nilai:", mahasiswa["nilai"]
    )


# 5. Menghitung rata-rata nilai
print("\n=== RATA-RATA NILAI ===")
rata_rata = rata_rata_nilai(data_mahasiswa)
print("Rata-rata nilai mahasiswa:", round(rata_rata, 2))
