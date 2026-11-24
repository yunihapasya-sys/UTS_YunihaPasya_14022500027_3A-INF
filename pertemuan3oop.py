# 1. Class & Objek Dasar
class AgensiDesain:
    pass

class Desainer:
    pass

studio_kreatif = AgensiDesain()
print(type(studio_kreatif))

peran_utama = Desainer()
print(type(peran_utama))


# 2. Instance Attribute
founder1 = Desainer()
founder1.nama = "Yuniha"
founder1.bidang = "Brand Identity"
print(founder1.nama)
print(founder1.bidang)

founder2 = Desainer()
founder2.nama = "Canda"
founder2.bidang = "UI/UX Design"
print(founder2.nama)
print(founder2.bidang)


# 3. Class Attribute (Atribut Bawaan Kelas)
class InfoAgensi:
    niche = "B2B Rebranding untuk Startup & UMKM Premium"
    sistem = "Hybrid / Remote Collaboration"

info = InfoAgensi()
print(info.niche)
print(info.sistem)


# 4. Class, Objek, & Method (Percakapan Bisnis)
class Founder:
    def __init__(self, nama, bidang, hobi):
        self.nama = nama
        self.bidang = bidang
        self.hobi = hobi

    def bicara(self, kalimat):
        print(f"{self.nama}: {kalimat}")

    # -- Bertemu --
    def minta_kursi(self):
        self.bicara("Permisi, kursi di depan kamu ini kosong nggak? Meja lain udah penuh semua.")

    def persilakan(self):
        self.bicara("Oh, kosong kok. Silakan, taruh aja tas di situ.")

    def puji_layar(self, lawan):
        self.bicara("Makasih ya. Eh, maaf nggak sengaja kelihatan layar kamu.. itu desain aplikasi, ya? "
                    "Hierarki visualnya rapi banget.")

    # -- Kenalan --
    def terima_pujian(self):
        self.bicara(f"Hehe, makasih. Itu masih revisi ketiga dari klien, jadi belum final. Saya {self.nama}, by the way.")

    def kenalan_balik(self, lawan):
        self.bicara(f"Salam kenal, {lawan.nama}. Saya {self.nama}. Kamu freelance atau ngantor?")

    def jelaskan_profesi(self):
        self.bicara(f"Freelance, fokus di {self.bidang}. Kamu sendiri? Dari tadi kayaknya lagi ngerjain logo, ya?")

    def jelaskan_profesi_balik(self):
        self.bicara(f"Ketahuan, hehe. Iya, saya di {self.bidang}: logo, palet warna, sama panduan brand. "
                    "Lagi ngerjain buat kedai kopi lokal.")

    def komentar_beda_lapisan(self):
        self.bicara("Wah, beda lapisan tapi nyambung ya. Brand dulu, baru diterjemahin ke tampilan aplikasi.")

    # -- Hobi --
    def tanya_hobi(self):
        self.bicara("Kalau lagi mentok, biasanya kamu cari inspirasinya dari mana?")

    def jawab_hobi(self, tambahan, tanya_balik=True):
        self.bicara(f"Saya suka {self.hobi}. {tambahan}"
                    + (" Kamu sendiri gimana?" if tanya_balik else ""))

    def tanggapi_hobi(self):
        self.bicara("Seru juga. Kayaknya cara kita nyari inspirasi beda, tapi hasilnya bisa saling melengkapi.")

    # -- Bangun agensi --
    def tanya_pengalaman_klien(self):
        self.bicara("Boleh nanya soal kerjaan nggak? Klien kamu biasanya udah punya brand, "
                    "atau sering disuruh bikinin sekalian?")

    def curhat_masalah(self):
        self.bicara("Sering banget disuruh sekalian, padahal itu bukan keahlian saya. Hasilnya ya seadanya.")

    def curhat_balik(self):
        self.bicara("Nah, saya kebalikannya. Klien minta logo, terus nanya, 'sekalian bikinin aplikasinya bisa nggak?' "
                    "Akhirnya sering saya tolak.")

    def lempar_ide(self):
        self.bicara("Berarti kalau digabung, klien tinggal datang ke satu tempat, ya? "
                    "Pernah kepikiran bikin agensi kecil independen bareng gitu?")

    def sambut_dengan_ragu(self):
        self.bicara("Jujur, pernah kepikiran juga. Cuma pasar agensi lagi padat banget. "
                    "Kita mau main di celah yang mana biar nggak tenggelam?")

    def usul_niche(self):
        self.bicara(f"Jangan semua segmen. Fokus ke {InfoAgensi.niche} aja: produknya udah bagus, "
                    "tapi visual dan aplikasinya belum rapi.")

    def setuju_dengan_catatan(self, lawan):
        self.bicara(f"Masuk akal. Pembagian kerjanya juga jelas: saya {self.bidang}, {lawan.nama} {lawan.bidang}. "
                    "Cuma PR-nya, kita belum punya portofolio atas nama agensi.")

    def usul_langkah_awal(self):
        self.bicara("Mulai kecil aja. Gabungin portofolio terbaik kita jadi satu pitch deck. "
                    "Habis itu tawarin revamp gratis ke dua brand lokal kenalan kita buat studi kasus.")

    def sepakat(self):
        self.bicara("Setuju, kita mulai dari situ. Boleh minta WhatsApp atau LinkedIn kamu? "
                    "Kita ketemu lagi Kamis sore buat mulai nyusun pitch deck.")

    def tutup(self, lawan):
        self.bicara(f"Boleh banget, nanti saya kirim nomornya. Sampai Kamis ya, {lawan.nama}!")


# Membuat objek tokoh (data diambil dari objek di bagian 2)
yuniha = Founder(founder1.nama, founder1.bidang,
                 "ngulik tipografi jadul dan eksperimen palet warna korporat")
canda = Founder(founder2.nama, founder2.bidang,
                "ngamatin interaksi mikro di aplikasi orang, kayak animasi tombol dan transisi halaman")

# -- Jalannya Percakapan --
print("\nPERCAKAPAN BISNIS DI CO-WORKING SPACE\n")

print("-- Bertemu di Meja yang Penuh --")
yuniha.minta_kursi()
canda.persilakan()
yuniha.puji_layar(canda)

print("\n-- Kenalan --")
canda.terima_pujian()
yuniha.kenalan_balik(canda)
canda.jelaskan_profesi()
yuniha.jelaskan_profesi_balik()
canda.komentar_beda_lapisan()

print("\n-- Sesi Obrolan Santai (Hobi & Inspirasi) --")
yuniha.tanya_hobi()
canda.jawab_hobi("Sering buka aplikasi orang cuma buat nonton transisinya.")
yuniha.jawab_hobi("Sering mampir ke pasar buku bekas buat motret sampul-sampul lawas.",
                  tanya_balik=False)
canda.tanggapi_hobi()

print("\n-- Sesi Kolaborasi & Ide Bisnis --")
yuniha.tanya_pengalaman_klien()
canda.curhat_masalah()
yuniha.curhat_balik()
canda.lempar_ide()
yuniha.sambut_dengan_ragu()
canda.usul_niche()
yuniha.setuju_dengan_catatan(canda)
canda.usul_langkah_awal()
yuniha.sepakat()
canda.tutup(yuniha)

print("\nPERCAKAPAN SELESAI, KEDUA FOUNDER SEPAKAT MEMBANGUN AGENSI\n")