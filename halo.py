nama = input("masukkan nama anda:")
print("halo", nama)

try:
    tahun_lahir = int(input("masukkan tahun lahir anda:"))
    usia = 2026 - tahun_lahir
    print("perkiraan usia anda:", usia, "tahun")
except ValueError:
    print("input harus berupa angka, contoh: 1990")