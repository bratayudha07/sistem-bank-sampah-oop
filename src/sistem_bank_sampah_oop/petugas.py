from __future__ import annotations

from typing import TYPE_CHECKING

from sistem_bank_sampah_oop.pengguna import Pengguna
from sistem_bank_sampah_oop.status_setoran import StatusSetoran

if TYPE_CHECKING:
    from sistem_bank_sampah_oop.setoran_sampah import SetoranSampah


class Petugas(Pengguna):
    """
    docstring
    """

    def __init__(self, id_petugas: str, nama: str, aktif: bool):
        super().__init__(id_petugas, nama)
        self._aktif = aktif

    @property
    def id_petugas(self):
        return self.id

    @id_petugas.setter
    def id_petugas(self, id_petugas: str):
        self.id = id_petugas

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nama: str):
        self._nama = nama

    @property
    def aktif(self):
        return self._aktif

    @aktif.setter
    def aktif(self, aktif: bool):
        self._aktif = aktif

    def tampilkan_profil(self) -> None:
        status = "Aktif" if self._aktif else "Tidak aktif"
        print(f"ID Petugas: {self.id_petugas}\nNama: {self.nama}\nStatus: {status}")

    def terima_setoran(self, setoran: SetoranSampah) -> None:
        if not self.validasi_setoran(setoran):
            raise ValueError("Setoran tidak valid untuk diterima.")
        setoran.terima()

    def validasi_setoran(self, setoran: SetoranSampah) -> bool:
        return (
            self._aktif
            and setoran.status is StatusSetoran.MENUNGGU
            and setoran.berat_kg > 0
        )
