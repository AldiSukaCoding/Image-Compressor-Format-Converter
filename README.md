# # Image Compressor & Format Converter
  Aplikasi desktop berbasis GUI (Antarmuka Grafis) yang ringan dan modern untuk melakukan kompresi ukuran memori sekaligus mengubah format gambar secara massal. Aplikasi ini dibangun menggunakan **Python** dengan antarmuka **CustomTkinter**, serta ditenagai oleh pustaka pemrosesan citra digital **Pillow (PIL)**.

---

## Fitur Utama
- **Antarmuka Modern:** Menggunakan tema bawaan CustomTkinter yang mendukung otomatisasi Mode Gelap/Terang (System Theme).
- **Pemrosesan Massal (Batch):** Mendukung pemilihan dan pemrosesan banyak file gambar sekaligus dalam satu antrean kerja.
- **Kompresi Slider Pintar:** Dilengkapi slider tingkat kualitas untuk memperkecil ukuran file gambar (JPEG/WebP) secara signifikan sesuai keinginan Anda.
- **Konversi Format Instan:** Mendukung konversi silang antar format gambar populer seperti `JPEG`, `PNG`, dan `WEBP` secara otomatis.
- **Bebas Hang/Freeze:** Proses konversi berjalan di latar belakang menggunakan teknik *Asynchronous Threading*, sehingga aplikasi tetap responsif selama proses berlangsung.
- **Konsol Log Real-time:** Menampilkan riwayat status pemrosesan dan perbandingan ukuran berkas sebelum serta sesudah dikompres dalam satuan Kilobyte (KB).

---

## Prasyarat & Dependensi
Sebelum menjalankan aplikasi ini, pastikan komputer Anda sudah terinstal pustaka dan komponen berikut:
### 1. Python
Pastikan Python versi 3.8 atau yang lebih baru sudah terpasang di sistem Anda.
### 2. Pustaka Python (Pip)
Instal pustaka yang dibutuhkan dengan menjalankan perintah berikut di terminal/command prompt:
```bash
pip install customtkinter Pillow
