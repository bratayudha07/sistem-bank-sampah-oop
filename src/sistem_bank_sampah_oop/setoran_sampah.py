from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING, Any

from sistem_bank_sampah_oop.enums import StatusSetoran

if TYPE_CHECKING:
    from sistem_bank_sampah_oop.jenis_sampah import JenisSampah
    from sistem_bank_sampah_oop.petugas import Petugas


class SetoranSampah:
    """
    docstring
    """

    def __init__(
        self,
        id_setoran: str,
        nasabah: Any,
        petugas: Petugas,
        jenis_sampah: JenisSampah,
        berat_kg: Decimal,
        tanggal: datetime,
        status: StatusSetoran,
    ):
        self.id_setoran = id_setoran
        self.nasabah = nasabah
        self.petugas = petugas
        self.jenis_sampah = jenis_sampah
        self.berat_kg = berat_kg
        self.tanggal = tanggal
        self.status = status
        self.alasan_penolakan: str | None = None

    def hitung_nilai(self) -> Decimal:
        return self.jenis_sampah.hitung_nilai(self.berat_kg)

    def terima(self) -> None:
        self._pastikan_pending()
        self.status = StatusSetoran.VERIFIED

    def tolak(self, alasan: str) -> None:
        self._pastikan_pending()
        self.alasan_penolakan = alasan
        self.status = StatusSetoran.REJECTED

    def _pastikan_pending(self) -> None:
        if self.status is not StatusSetoran.PENDING:
            raise ValueError("Hanya setoran berstatus PENDING yang dapat diproses.")
