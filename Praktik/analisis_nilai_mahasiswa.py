
def rata_rata(data):
    """Menghitung rata-rata dan menangani list kosong."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    """Mengembalikan list nilai yang memenuhi batas kelulusan."""
    hasil = []

    for x in data:
        if x >= batas:
            hasil.append(x)

    return hasil


# Data nilai 10 mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Mengolah data
lulus = nilai_lulus(nilai)
jumlah_data = len(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = jumlah_data - jumlah_lulus

# Menampilkan hasil analisis
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Data nilai       : {nilai}")
print(f"Banyak data      : {jumlah_data}")
print(f"Total nilai      : {sum(nilai)}")
print(f"Rata-rata        : {rata_rata(nilai):.2f}")
print(f"Nilai minimum    : {min(nilai)}")
print(f"Nilai maksimum   : {max(nilai)}")
print(f"Nilai lulus      : {lulus}")
print(f"Jumlah lulus     : {jumlah_lulus}")
print(f"Belum lulus      : {jumlah_belum_lulus}")


print("\n=== TEST CASE ===")

print("Rata-rata [60, 70, 80] =", rata_rata([60, 70, 80]))
print("Minimum [60, 70, 80] =", min([60, 70, 80]))
print("Maksimum [60, 70, 80] =", max([60, 70, 80]))
print("Jumlah lulus [60, 70, 80] =", len(nilai_lulus([60, 70, 80])))
print("Jumlah lulus [59, 60, 61] =", len(nilai_lulus([59, 60, 61])))
print("Rata-rata list kosong =", rata_rata([]))
