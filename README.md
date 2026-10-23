# Pertemuan 09 — List dan Pengolahan Data Numerik

## Identitas Mahasiswa

- **Nama:** Anastasya Putri Kirana
- **NIM:** 2225250041
- **Kelas:** 3A
- **Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan

Mempelajari penggunaan list Python untuk menyimpan, mengakses, memodifikasi, dan mengolah kumpulan data numerik. Praktik ini juga menggabungkan list dengan perulangan, seleksi, dan fungsi untuk menghitung statistik serta menganalisis kelulusan mahasiswa.

## Struktur Program

```text
pertemuan-09-list-2225250041/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

## Deskripsi Latihan

1. **Membuat dan Membaca List:** Menyimpan nilai dalam list dan menghitung jumlah elemen menggunakan `len()`.
2. **Indeks dan Slicing:** Mengakses elemen pertama, elemen terakhir, dan bagian tertentu dari list.
3. **Manipulasi List:** Mengubah, menambahkan, menyisipkan, dan menghapus elemen.
4. **Agregasi Nilai:** Menghitung total, rata-rata, nilai minimum, dan maksimum.
5. **Filter Kelulusan:** Memilih nilai yang memenuhi batas kelulusan 60.
6. **Fungsi Statistik:** Menghitung rata-rata menggunakan fungsi dan menangani list kosong.

## Praktik Analisis Nilai Mahasiswa

Program menggunakan list yang berisi 10 nilai mahasiswa. Program menghitung banyak data, total, rata-rata, nilai minimum, nilai maksimum, jumlah mahasiswa lulus, jumlah mahasiswa belum lulus, dan membuat list baru berisi nilai yang lulus.

Batas kelulusan yang digunakan adalah 60. Program menggunakan fungsi `rata_rata(data)` dan `nilai_lulus(data, batas=60)` untuk mengolah data.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal dari folder utama project:

```bash
python latihan/01_buat_list.py
python latihan/02_indeks_slicing.py
python latihan/03_manipulasi_list.py
python latihan/04_agregasi_nilai.py
python latihan/05_filter_kelulusan.py
python latihan/06_fungsi_statistik.py
python praktik/analisis_nilai_mahasiswa.py
```

## Hasil Pengujian

| Data | Pengujian | Hasil Aktual |
|---|---|---|
| `[60, 70, 80]` | Rata-rata | 70.0 |
| `[60, 70, 80]` | Minimum | 60 |
| `[60, 70, 80]` | Maksimum | 80 |
| `[60, 70, 80]` | Jumlah lulus | 3 |
| `[59, 60, 61]` | Jumlah lulus | 2 |
| `[]` | Rata-rata list kosong | 0 |

Seluruh hasil pengujian di atas sesuai dengan hasil yang diharapkan pada modul.

## Refleksi

Melalui praktikum ini, saya mempelajari cara menyimpan banyak data dalam satu list, mengakses elemen menggunakan indeks, memodifikasi list, dan menghitung statistik menggunakan fungsi bawaan Python. Saya juga memahami cara menggabungkan list dengan perulangan, seleksi, dan fungsi untuk menganalisis kelulusan mahasiswa. Salah satu hal penting yang dipelajari adalah perlunya menangani list kosong agar perhitungan rata-rata tidak menghasilkan error.

