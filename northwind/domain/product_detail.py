from dataclasses import dataclass
from abc import ABC, abstractclassmethod
from typing import List
from northwind.seedwork.entity import Entity
from northwind.seedwork.i_command import ICommand

@dataclass
class ProductDetail(Entity):
    __slots__ = [
        'name',
        'quantity_per_unit',
        'unit_price',
        'units_in_stock',
        'units_on_order',
        'reorder_level',
        'discontinued',
        'category_name',
        'category_description',
        'supplier_name',
        'supplier_region'
    ]
    name: str
    quantity_per_unit: int
    unit_price: float
    units_in_stock: int
    units_on_order: int
    reorder_level: int
    discontinued: int
    category_name: str
    category_description: str
    supplier_name: str
    supplier_region: str
    MAX_UNIT_PRICE = 10000.0

@dataclass
class SearchForProductDetails(ICommand):
    __slots__ = [
        'name',
        'unit_price_from',
        'unit_price_to',
        'category_name'
    ]
    name: str
    unit_price_from: float
    unit_price_to: float
    category_name: str

    def __post_init__(self):
        if self.unit_price_from is None:
            self.unit_price_from = 0
        if self.unit_price_to is None:
            self.unit_price_to = ProductDetail.MAX_UNIT_PRICE
        if self.unit_price_from > self.unit_price_to:
           raise InvalidUnitPriceRangeException

class InvalidCategoryException(Exception):
    def __init__(self) -> None:
        super().__init__('Invalid Category')

class InvalidUnitPriceRangeException(Exception):
    def __init__(self) -> None:
        super().__init__('Unit Price To must be higher than Unit Price From')

class IProductDetailRepository(ABC):

    @abstractclassmethod
    def find(
        name: str,
        unit_price_from: float,
        unit_price_to: float,
        category_name: str
        ) -> List[ProductDetail]:        
        pass