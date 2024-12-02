# import fungsi date

import datetime as dt
from datetime import date

def hitung_usia_dalam_tahun_dan_bulan():
    try:
        # Memasukkan data tanggal lahir
        tanggal = int(input("Masukkan tanggal lahir : "))
        bulan = int(input("Masukkan bulan lahir : "))
        tahun = int(input("Masukkan tahun lahir: "))
        
        # Konversi input ke tipe data date
        tanggal_lahir = date(tahun, bulan, tanggal)
        
        # Mendapatkan tanggal hari ini
        hari_ini = date.today()
        
        # Menghitung total hari sejak tanggal lahir
        total_hari = (hari_ini - tanggal_lahir).days
        
        # Menghitung total hari sejak tanggal lahir
        total_hari = (hari_ini - tanggal_lahir).days
        print(f"Total hari sejak tanggal lahir = {total_hari} hari")
        
        # Membagi total hari dengan 365 untuk mendapatkan tahun
        tahun_usia = total_hari // 365
        sisa_hari = total_hari % 365  # Sisa hari setelah dibagi 365
        
        # Menghitung bulan berdasarkan sisa hari (anggap rata-rata bulan = 30 hari)
        bulan_usia = sisa_hari // 30
        sisa_hari %= 30
        
        # Menghitung bulan berdasarkan sisa hari (anggap rata-rata bulan = 30 hari)
        bulan_usia = sisa_hari // 30
        sisa_hari %= 30
                # Membagi total hari dengan 365 untuk mendapatkan tahun
        total_tahun = total_hari // 365
        sisa_hari = total_hari % 365  # Sisa hari setelah dibagi 365
        # Menampilkan hasil
        print(f"Usia Anda adalah: {total_tahun} tahun, {bulan_usia} bulan, dan {sisa_hari} hari.")
        
    except ValueError as e:
        print(f"Terjadi kesalahan: {e}. Pastikan Anda memasukkan tanggal, bulan, dan tahun yang valid.")
# Memanggil fungsi
hitung_usia_dalam_tahun_dan_bulan()