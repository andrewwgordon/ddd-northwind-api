from northwind.adapter.configuration import application
from northwind.domain.product_detail import SearchForProductDetails
from northwind.service.service_manager import ServiceManager

def test_service_manager():
    product_detail_repository = application.get_product_detail_repository()
    service_manager = ServiceManager(product_detail_repository)
    search_for_product_details = SearchForProductDetails(
        None,None,None,'Beverages'
    )
    results = service_manager.handle(search_for_product_details)
    if results is not None:
        print(results)
        assert results[0].name == 'Chai'
    else:
        assert 1 == 0

