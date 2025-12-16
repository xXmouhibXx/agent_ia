import pytest
from book import (
    get_book_price,
    calculate_discounted_price,
    calculate_total_price,
    combine_prices,
    books # Needed for setup/teardown if tests were modifying it, but generally good to have context.
)

# A common pattern for managing mutable global state in tests is to save and restore it,
# or to use fixtures that provide a known state.
# For this simple case, we'll assume `books` remains constant during test runs.

def test_get_book_price_existing_book():
    """Test retrieving the price of an existing book."""
    assert get_book_price("python_guide") == 25.99
    assert get_book_price("data_science") == 32.50
    assert get_book_price("algorithms") == 45.00

def test_get_book_price_non_existing_book():
    """Test retrieving the price of a non-existing book, expecting 0."""
    assert get_book_price("non_existent_book") == 0
    assert get_book_price("unknown") == 0

@pytest.mark.parametrize("book_name, discount_percent, expected_price", [
    ("python_guide", 10, 23.391),  # 25.99 * (1 - 0.1)
    ("data_science", 25, 24.375),  # 32.50 * (1 - 0.25)
    ("web_dev", 0, 28.75),        # No discount
    ("algorithms", 100, 0),       # 100% discount
    ("machine_learning", 50, 27.625), # 55.25 * (1 - 0.5)
    ("python_guide", -10, 28.589), # Negative discount (price increase)
])
def test_calculate_discounted_price_valid_book(book_name, discount_percent, expected_price):
    """Test calculating discounted price for existing books with various discounts."""
    # Use pytest.approx for float comparisons
    assert calculate_discounted_price(book_name, discount_percent) == pytest.approx(expected_price)

def test_calculate_discounted_price_non_existing_book():
    """Test calculating discounted price for a non-existing book, expecting 0."""
    assert calculate_discounted_price("non_existent_book", 10) == 0
    assert calculate_discounted_price("unknown_book", 50) == 0

@pytest.mark.parametrize("book_list, expected_total", [
    ([], 0),                                # Empty list
    (["python_guide"], 25.99),              # Single existing book
    (["python_guide", "data_science"], 25.99 + 32.50), # Multiple existing books
    (["non_existent"], 0),                  # Single non-existing book
    (["python_guide", "non_existent"], 25.99), # Mix of existing and non-existing
    (["non_existent1", "non_existent2"], 0), # All non-existing
    (["web_dev", "algorithms", "machine_learning"], 28.75 + 45.00 + 55.25), # More books
])
def test_calculate_total_price(book_list, expected_total):
    """Test calculating total price for various lists of books."""
    assert calculate_total_price(book_list) == pytest.approx(expected_total)

@pytest.mark.parametrize("book1, book2, expected_combined_price", [
    # Both books exist, 10% discount applies
    ("python_guide", "data_science", (25.99 + 32.50) * 0.9),
    ("web_dev", "algorithms", (28.75 + 45.00) * 0.9),
    ("python_guide", "python_guide", (25.99 + 25.99) * 0.9), # Same book twice

    # One book exists, one does not (no discount, sum of prices)
    ("python_guide", "non_existent", 25.99 + 0),
    ("non_existent", "data_science", 0 + 32.50),

    # Neither book exists (sum of zeros)
    ("non_existent1", "non_existent2", 0 + 0),
    ("unknown1", "unknown2", 0),
])
def test_combine_prices(book1, book2, expected_combined_price):
    """Test combining prices of two books with and without bundle discount."""
    assert combine_prices(book1, book2) == pytest.approx(expected_combined_price)