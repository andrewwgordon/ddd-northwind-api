SQL='''
select
    Id,
    ProductName,
    QuantityPerUnit,
    UnitPrice,
    UnitsInStock,
    UnitsOnOrder,
    ReOrderLevel,
    Discontinued,
    CategoryName,
    CategoryDescription,
    SupplierName,
    SupplierRegion
from ProductDetails_V
where
    ProductName like ?
and
    UnitPrice >= ?
and
    UnitPrice <= ?
and
    CategoryName like ?
'''