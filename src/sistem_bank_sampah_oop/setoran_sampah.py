from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sistem_bank_sampah_oop.status_setoran import StatusSetoran

if TYPE_CHECKING:
    from sistem_bank_sampah_oop.jenis_sampah import JenisSampah
    from sistem_bank_sampah_oop.petugas import Petugas


class SetoranSampah:
    def __init__(
        self,
        id_setoran: str,
        jenis_sampah: JenisSampah,
        berat_kg: Decimal,
        tanggal: datetime,
        petugas: Petugas,
        status: StatusSetoran = StatusSetoran.MENUNGGU,
    ):
        self.id_setoran = id_setoran
        self.jenis_sampah = jenis_sampah
        self.berat_kg = berat_kg
        self.tanggal = tanggal
        self.petugas = petugas
        self.status = status
        self.alasan_penolakan: str | None = None

    def hitung_berat(self) -> Decimal:
        return self.berat_kg

    def terima(self) -> None:
        self._pastikan_menunggu()
        self.status = StatusSetoran.DITERIMA

    def tolak(self, alasan: str) -> None:
        self._pastikan_menunggu()
        self.alasan_penolakan = alasan
        self.status = StatusSetoran.DITOLAK

    def _pastikan_menunggu(self) -> None:
        if self.status is not StatusSetoran.MENUNGGU:
            raise ValueError("Hanya setoran berstatus MENUNGGU yang dapat diproses.")
