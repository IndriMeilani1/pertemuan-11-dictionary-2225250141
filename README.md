# Pertemuan 11 - Dictionary/Map
Nama: Indri Meilani
NIM: 2225250141
Kelas: 3A

## Tujuan
Tujuan dari program ini adalah untuk memodelkan dan mengelola data pendidikan menggunakan dictionary dalam Python. Program ini dibuat agar data mahasiswa, seperti NIM, nama, kelas, dan nilai, dapat disimpan, dicari, ditambahkan, diperbarui, serta ditampilkan dengan mudah. Selain itu, program juga digunakan untuk menghitung rata-rata nilai seluruh mahasiswa.

## Struktur Data
Struktur data yang digunakan adalah dictionary dengan NIM sebagai key utama karena setiap mahasiswa memiliki NIM yang berbeda. Sementara itu, value berupa dictionary yang berisi informasi mahasiswa, yaitu nama, kelas, dan nilai. Contohnya, NIM A001 digunakan sebagai key, sedangkan Ayu, kelas A, dan nilai 85 menjadi value di dalamnya. Dengan menggunakan struktur ini, data mahasiswa dapat dicari secara langsung berdasarkan NIM tanpa harus menggunakan indeks seperti pada list.

## Cara Menjalankan
python3 praktik/data_mahasiswa.py

## Test Case
Pengujian dilakukan dengan beberapa kondisi. Pertama, pencarian mahasiswa menggunakan NIM A003 dengan hasil yang diharapkan yaitu data mahasiswa bernama Citra, kelas B, dan nilai 92 dapat ditampilkan, dan hasil aktual sesuai dengan harapan (Berhasil). Kedua, penambahan mahasiswa dengan NIM A006, nama Fani, kelas B, dan nilai 90. Hasil yang diharapkan adalah data berhasil ditambahkan ke dalam dictionary dan hasil aktual menunjukkan bahwa data berhasil ditambahkan (Berhasil). Ketiga, pembaruan nilai mahasiswa dengan NIM A002 dari 78 menjadi 82. Hasil yang diharapkan adalah nilai Budi berubah menjadi 82 dan hasil aktual sesuai dengan harapan (Berhasil). Keempat, program menampilkan seluruh data mahasiswa menggunakan items() dan semua NIM beserta informasi mahasiswa berhasil ditampilkan (Berhasil). Terakhir, program menghitung rata-rata nilai setelah penambahan dan pembaruan data. Hasil yang diharapkan adalah rata-rata sebesar 85,17 dan hasil aktual menunjukkan nilai yang sama (Berhasil).

## Refleksi
Kesalahan yang dapat ditemukan saat menggunakan dictionary adalah ketika mengakses key yang tidak tersedia, misalnya memanggil data_mahasiswa["A999"], padahal NIM tersebut belum terdaftar. Kesalahan ini dapat menyebabkan program mengalami KeyError. Untuk memperbaikinya, saya menggunakan method get() atau memeriksa keberadaan key terlebih dahulu menggunakan operator in. Dengan cara tersebut, program dapat menampilkan pesan bahwa data mahasiswa tidak ditemukan tanpa menyebabkan program berhenti. Dari latihan ini, saya memahami bahwa penggunaan dictionary harus memperhatikan keberadaan key agar proses pencarian dan pengolahan data berjalan dengan baik.
