from __future__ import annotations

from typing import TYPE_CHECKING
from sistem_bank_sampah_oop.pengguna import Pengguna

if TYPE_CHECKING:
    from sistem_bank_sampah_oop.setoran_sampah import SetoranSampah


class Petugas(Pengguna):
    """Class Petugas yang merupakan turunan (inheritance) dari Pengguna."""

    def __init__(self, id: str, nama: str, aktif: bool):
        super().__init__(id, nama)
        self.__aktif = aktif  # Private attribute (-aktif)

    @property
    def aktif(self) -> bool:
        return self.__aktif

    @aktif.setter
    def aktif(self, status: bool) -> None:
        self.__aktif = status

    def tampilkan_profil(self) -> str:
        """Overriding method untuk menampilkan profil petugas (+tampilkan_profil() str)"""
        status_str = "Aktif" if self.__aktif else "Tidak Aktif"
        return f"ID: {self._id} | Nama: {self._nama} | Status: {status_str}"

    def validasi_setoran(self, setoran: SetoranSampah) -> bool:
        """Validasi setoran yang masuk (+validasi_setoran(setoran) bool)"""
        from sistem_bank_sampah_oop.status_setoran import StatusSetoran

        # Petugas harus aktif, berat > 0, dan status setoran masih MENUNGGU
        return (
            self.__aktif
            and setoran.berat_kg > 0
            and setoran.status == StatusSetoran.MENUNGGU
        )
