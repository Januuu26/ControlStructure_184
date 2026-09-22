nilai = float(input("Masukkan persentase nilai mahasiswa: "))

if nilai >= 90:
    print("Excellent")
elif nilai >= 80:
    print("Very Good")
elif nilai >= 70:
    print("Good")
elif nilai >= 60:
    print("Average")
else:
    print("Below average")