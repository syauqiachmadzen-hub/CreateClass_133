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


objek_jajar = Jajargenjang(10, 5, 7)
print(objek_jajar)

print("Keliling:", objek_jajar.hitung_keliling(), "cm")
print("Luas:", objek_jajar.hitung_luas(), "cm2")