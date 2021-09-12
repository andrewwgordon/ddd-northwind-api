import connexion
import logging
from northwind.adapter.configuration import application
from northwind.domain.product_detail import SearchForProductDetails

log=logging.getLogger(__name__)

service_manager = application.get_service_manager()

def search(
        name: str=None,
        unit_price_from: float=None,
        unit_price_to: float=None,
        category_name: str=None
        ):
    try:
        search_for_product_details = SearchForProductDetails(
            name,unit_price_from,unit_price_to,category_name
        )
        results = service_manager.handle(search_for_product_details)
        if results is not None:
            return results
        else:
            return ('Not Found',404)
    except Exception as ex:
        log.error(ex.args[0])
        return (ex.args[0],500)