from decimal import Decimal


class JenisSampah:
    """
    docstring
    """

    def __init__(self, id_jenis: str, nama: str, harga_per_kg: Decimal, aktif: bool):
        self.id_jenis = id_jenis
        self.nama = nama
        self.harga_per_kg = harga_per_kg
        self.aktif = aktif

    def ubah_harga(self, harga: Decimal) -> None:
        self.harga_per_kg = harga

    def hitung_nilai(self, berat: Decimal) -> Decimal:
        return self.harga_per_kg * berat
