a = float(input("Suku pertama (a): "))
d = float(input("Beda (d): "))
n = int(input("Jumlah suku (n): "))

while n <= 0:
    print("n harus lebih dari 0.")
    n = int(input("Jumlah suku (n): "))

total = 0

for i in range(n):
    suku = a + i * d
    print(suku)
    total += suku

print(f"Jumlah = {total}")