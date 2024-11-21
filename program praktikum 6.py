def hitung_nilai_akhir(tugas, uts, uas):
    # Menghitung nilai akhir berdasarkan bobot masing-masing komponen
    return tugas * 0.30 + uts * 0.35 + uas * 0.35

def tampilkan_tabel(daftar_mahasiswa):
    # Menampilkan tabel hasil perhitungan
    print("\n| No | Nama        | NIM        | Tugas | UTS  | UAS  | Nilai Akhir |")
    print("|----|-------------|------------|-------|------|------|-------------|")
    for idx, mahasiswa in enumerate(daftar_mahasiswa, start=1):
        print(f"| {idx:<2} | {mahasiswa['Nama']:<10} | {mahasiswa['NIM']:<10} | {mahasiswa['Tugas']:<5} | {mahasiswa['UTS']:<5} | {mahasiswa['UAS']:<5} | {mahasiswa['Nilai Akhir']:<11.2f} |")

def main():
    # List untuk menyimpan data mahasiswa
    daftar_mahasiswa = []
    
    while True:
        # Meminta input Nama, NIM, Nilai Tugas, UTS, dan UAS
        nama = input("Nama: ")
        nim = input("NIM: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        
        # Menghitung nilai akhir
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        
        # Menambahkan data mahasiswa ke dalam daftar
        daftar_mahasiswa.append({
            'Nama': nama,
            'NIM': nim,
            'Tugas': tugas,
            'UTS': uts,
            'UAS': uas,
            'Nilai Akhir': nilai_akhir
        })
        
        # Menanyakan apakah ingin menambah data
        tambah_data = input("Tambah data? (y/t): ").lower()
        
        if tambah_data == 't':
            break
    
    # Menampilkan tabel hasil perhitungan nilai akhir
    tampilkan_tabel(daftar_mahasiswa)

# Memanggil fungsi utama
main()
