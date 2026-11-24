class Murid:
    nidn = 0
    nama = ""
     
    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")
        
    def hello(self, nama):
        print(f"Halo {self.nama}, nama saya {nama}")
        
Murid = Murid()
Murid.nama = "yuniha"
Murid.perkenalan()
Murid.hello("canda") 