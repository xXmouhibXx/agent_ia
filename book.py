# Dictionary of books with their prices
books = {
    "python_guide": 25.99,
    "data_science": 32.50,
    "web_dev": 28.75,
    "algorithms": 45.00,
    "machine_learning": 55.25
}

def get_book_price(book_name):
    """Get price of a specific book."""
    return books.get(book_name, 0)

def calculate_discounted_price(book_name, discount_percent):
    """Calculate price after discount."""
    price = get_book_price(book_name)
    if price == 0:
        return 0
    return price * (1 - discount_percent / 100)

def calculate_total_price(book_list):
    """Calculate total price for multiple books."""
    total = 0
    for book in book_list:
        total += get_book_price(book)
    return total

def combine_prices(book1, book2):
    """Combine prices of two books with bundle discount."""
    price1 = get_book_price(book1)
    price2 = get_book_price(book2)
    
    if price1 == 0 or price2 == 0:
        return price1 + price2
    
    # Apply 10% bundle discount
    return (price1 + price2) * 0.9