from northwind.adapter.http_rest import product_details_controller

def test_product_details_controller():
    results = product_details_controller.search(None,None,None,'Beverages')
    if results is not None:
        assert results[0].name == 'Chai'
    else:
        assert 1 == 0