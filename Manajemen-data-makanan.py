class Resep:
    def __init__(self, nama, alat, bahan, langkah):
        self.nama = nama
        self.alat = alat
        self.bahan = bahan
        self.langkah = langkah
    
    def tampilkan_resep(self):
        print("\n" + "="*50)
        print(f"RESEP {self.nama.upper()}")
        print("="*50)
        
        print("\nALAT YANG DIBUTUHKAN:")
        for i, alat in enumerate(self.alat, 1):
            print(f"   {i}. {alat}")
        
        print("\nBAHAN-BAHAN:")
        for i, bahan in enumerate(self.bahan, 1):
            print(f"   {i}. {bahan}")
        
        print("\nCARA MEMASAK:")
        for i, langkah in enumerate(self.langkah, 1):
            print(f"   {i}. {langkah}")
        
        print("\n" + "="*50)