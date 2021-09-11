from dataclasses import dataclass

@dataclass
class Entity:
    __slots__ = ['id']
    id: int