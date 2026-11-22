from product import product_details

def test_product_details():
    assert product_details(101, "Laptop", 2, 50000) == (
        "Product ID: 101\n"
        "Name: Laptop\n"
        "Quantity: 2\n"
        "Price: ₹50000.00"
    )