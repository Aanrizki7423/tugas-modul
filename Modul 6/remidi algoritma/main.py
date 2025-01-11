# Input Manual dari Pengguna
print("Masukkan data pegawai:")
nama = input("Nama: ")
gaji_pokok = float(input("Gaji Pokok: "))
durasi_lembur = int(input("Durasi Lembur (jam): "))
status = input("Status Pegawai (Tetap/Tidak Tetap): ").lower()

if status == "tetap":
    # Hitung Tunjangan dan Lembur untuk Pegawai Tetap
    tunjangan = 0.7 * gaji_pokok
    lembur = durasi_lembur * (0.1 * gaji_pokok)
    gaji_bersih = gaji_pokok + tunjangan + lembur

    # Tampilkan informasi pegawai tetap
    print("\nInformasi Pegawai:")
    print(f"Nama: {nama}")
    print(f"Gaji Pokok: {gaji_pokok}")
    print(f"Tunjangan: {tunjangan}")
    print(f"Durasi Lembur: {durasi_lembur} jam")
    print(f"Gaji Bersih: {gaji_bersih}")

elif status == "tidak tetap":
    # Hitung Lembur untuk Pegawai Tidak Tetap
    lembur = durasi_lembur * (0.05 * gaji_pokok)
    gaji_bersih = gaji_pokok + lembur

    # Tampilkan informasi pegawai tidak tetap
    print("\nInformasi Pegawai:")
    print(f"Nama: {nama}")
    print(f"Gaji Pokok: {gaji_pokok}")
    print(f"Tunjangan: Tidak Ada")
    print(f"Durasi Lembur: {durasi_lembur} jam")
    print(f"Gaji Bersih: {gaji_bersih}")

else:
    print("Status pegawai tidak valid.")