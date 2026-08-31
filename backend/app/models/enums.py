import enum


class MaterialType(str, enum.Enum):
    PLASTIC = "plastic"
    GLASS = "glass"
    METAL = "metal"
    PAPER = "paper"
    ELECTRONICS = "electronics"
    OIL = "oil"
    ORGANIC = "organic"


class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"


class PointStatus(str, enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class SuggestionStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
