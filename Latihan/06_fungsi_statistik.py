
def rata_rata(data):
    # Menangani list kosong
    if len(data) == 0:
        return 0

    # Menghitung rata-rata
    return sum(data) / len(data)


nilai = [75, 80, 65, 90, 88]

print(f"Rata-rata = {rata_rata(nilai):.2f}")
