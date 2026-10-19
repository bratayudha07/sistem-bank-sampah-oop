from enum import Enum

class StatusSetoran(Enum):
    PENDING = "Pending"
    VERIFIED = "Verified"
    REJECTED = "Rejected"

class JenisMutasi(Enum):
    KREDIT = "Kredit"
    DEBIT = "Debit"