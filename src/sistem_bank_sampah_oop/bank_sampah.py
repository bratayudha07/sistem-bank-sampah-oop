from .enums import StatusSetoran, JenisMutasi

class BankSampah:
    def __init__(self, nama: str, alamat: str):
        self.nama = nama
        self.alamat = alamat
        
        # Aggregation: BankSampah menampung daftar objek lain
        self.daftar_nasabah = []
        self.daftar_petugas = []
        self.daftar_jenis_sampah = []
        self.daftar_setoran = []

    def tambah_nasabah(self, nasabah):
        self.daftar_nasabah.append(nasabah)

    def tambah_petugas(self, petugas):
        self.daftar_petugas.append(petugas)

    def tambah_jenis_sampah(self, jenis_sampah):
        self.daftar_jenis_sampah.append(jenis_sampah)

    def catat_setoran(self, setoran):
        self.daftar_setoran.append(setoran)