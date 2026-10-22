class JenisSampah:
    def __init__(
        self,
        id_jenis: str,
        nama: str,
        kategori: str,
        dapat_didaur_ulang: bool,
    ):
        self.id_jenis = id_jenis
        self.nama = nama
        self.kategori = kategori
        self.dapat_didaur_ulang = dapat_didaur_ulang

    def ubah_kategori(self, kategori: str) -> None:
        self.kategori = kategori

    def info_sampah(self) -> str:
        status_daur_ulang = "Ya" if self.dapat_didaur_ulang else "Tidak"
        return (
            f"ID: {self.id_jenis}\n"
            f"Nama: {self.nama}\n"
            f"Kategori: {self.kategori}\n"
            f"Dapat didaur ulang: {status_daur_ulang}"
        )
