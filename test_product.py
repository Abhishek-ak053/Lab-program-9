from product import product_details

def test_product_details():
    result = product_details("101", "Laptop", "2", "50000.00")

    expected = "Product ID: 101\nProduct Name: Laptop\nQuantity: 2\nPrice: 50000.00"

    assert result == expected
