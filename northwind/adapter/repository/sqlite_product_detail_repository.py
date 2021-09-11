from northwind.adapter.repository.sqlite_datastore_context import SQLiteDatastoreContext
from northwind.domain.product_detail import ProductDetail,IProductDetailRepository
from northwind.adapter.repository.sqlite_sql import find_product_details_query
from typing import List
import logging

log = logging.getLogger(__name__)

class SQLiteProductDetailRepository(IProductDetailRepository):

    def __init__(self,datastore_context: SQLiteDatastoreContext) -> None:
        self.__datastore_context = datastore_context

    def find(self,
        name: str,
        unit_price_from: float,
        unit_price_to: float,
        category_name: str
        ) -> List[ProductDetail]:  
        if category_name is None:
            category_name = '%'
        if name is None:
            name = '%'
        conn = self.__datastore_context.get_connection()
        try:            
            cur = conn.execute(
                find_product_details_query.SQL,
                (name,unit_price_from,unit_price_to,category_name)
            )
            product_details=[]
            for row in cur:
                product_details.append(
                    ProductDetail(
                        row[0],row[1],row[2],row[3],row[4],row[5],
                        row[6],row[7],row[8],row[9],row[10],row[11]
                    )
                )
        except Exception as ex:
            log.error(ex.args[0])
            raise ex
        finally:
            self.__datastore_context.close_connection(conn)
            if len(product_details) > 0:
                return product_details
            else:
                return None
