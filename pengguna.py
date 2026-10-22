from abc import ABC, abstractmethod


class Pengguna(ABC):
    """Abstract Class untuk dasar entitas pengguna sistem."""

    def __init__(self, id: str, nama: str):
        self._id = id      # Protected attribute (#id)
        self._nama = nama  # Protected attribute (#nama)

    @property
    def id(self) -> str:
        return self._id

    @property
    def nama(self) -> str:
        return self._nama

    @abstractmethod
    def tampilkan_profil(self) -> str:
        """Abstract method untuk menampilkan profil pengguna (+tampilkan_profil() str)"""
        pass
