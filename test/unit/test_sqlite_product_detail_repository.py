from northwind.adapter.configuration import application

def test_sqlite_product_detail_repository():
    prod_detail_repository = application.get_product_detail_repository()
    product_details = prod_detail_repository.find('%',0,10000,'Beverages')
    print(product_details)
    if product_details is not None:
        assert product_details[0].name == 'Chai'
    else:
        assert 1 == 0