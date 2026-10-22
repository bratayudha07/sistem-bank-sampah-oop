from __future__ import annotations

from typing import TYPE_CHECKING

from sistem_bank_sampah_oop.enums import StatusSetoran

if TYPE_CHECKING:
    from sistem_bank_sampah_oop.setoran_sampah import SetoranSampah


class Petugas:
    """
    docstring
    """

    def __init__(self, id_petugas: str, nama: str, aktif: bool):
        self._id_petugas = id_petugas
        self._nama = nama
        self._aktif = aktif

    @property
    def id_petugas(self):
        return self._id_petugas

    @id_petugas.setter
    def id_petugas(self, id_petugas: str):
        self._id_petugas = id_petugas

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

    def terima_setoran(self, setoran: SetoranSampah) -> None:
        if not self.validasi_setoran(setoran):
            raise ValueError("Setoran tidak valid untuk diterima.")
        setoran.terima()

    def validasi_setoran(self, setoran: SetoranSampah) -> bool:
        return (
            self._aktif
            and setoran.status is StatusSetoran.PENDING
            and setoran.berat_kg > 0
            and setoran.jenis_sampah.aktif
        )
