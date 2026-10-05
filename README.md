# Program OOP Python: Kalkulator Luas dan Keliling Jajargenjang

Program sederhana berbasis Python yang menerapkan konsep **Pemrograman Berorientasi Objek (OOP)** untuk menghitung luas dan keliling bangun datar **jajargenjang**.

---

## 🚀 Fitur Program
* **Berbasis Objek (OOP):** Menggunakan class `Jajargenjang` dengan enkapsulasi atribut dan method yang terstruktur.
* **Validasi Input:** Memastikan nilai alas, tinggi, dan sisi miring yang dimasukkan harus berupa angka positif ($> 0$).
* **Penanganan Error (`try-except`):** Mencegah program *crash* jika pengguna salah memasukkan tipe data (misalnya memasukkan huruf/simbol).
* **Magic Method (`__str__`):** Menampilkan representasi string objek secara otomatis dan informatif.

---

## 📐 Rumus Matematika
* **Luas ($L$):** $\text{Alas} \times \text{Tinggi}$
* **Keliling ($K$):** $2 \times (\text{Alas} + \text{Sisi Miring})$

---

## 💻 Contoh Kode Program

```python
class Jajargenjang:
    def __init__(self, alas, tinggi, sisi_miring):
        self.alas = alas
        self.tinggi = tinggi
        self.sisi_miring = sisi_miring

    def hitung_keliling(self):
        return 2 * (self.alas + self.sisi_miring)

    def hitung_luas(self):
        return self.alas * self.tinggi

    def __str__(self):
        return f"jajargenjang, alas {self.alas} cm, tinggi {self.tinggi} cm, dan sisi miring {self.sisi_miring} cm"

# Contoh Pengujian Langsung dengan Objek
objek_jajar = Jajargenjang(10, 5, 7)
print(objek_jajar)

print("Keliling:", objek_jajar.hitung_keliling(), "cm")
print("Luas:", objek_jajar.hitung_luas(), "cm2")