from abc import ABC, abstractmethod


class Pengguna(ABC):
    """
    docstring
    """

    def __init__(self, id: str, nama: str):
        self.id = id
        self.nama = nama

    @abstractmethod
    def tampilkan_profil(self):
        pass
