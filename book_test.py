import pytest
from book import (
    get_book_price,
    calculate_discounted_price,
    calculate_total_price,
    combine_prices,
)

# Tests for get_book_price function
def test_get_book_price_valid_book():
    """Test that get_book_price returns the correct price for an existing book."""
    assert get_book_price("python_guide") == pytest.approx(25.99)
    assert get_book_price("algorithms") == pytest.approx(45.00)

def test_get_book_price_invalid_book():
    """Test that get_book_price returns 0 for a non-existent book."""
    assert get_book_price("non_existent_book") == 0
    assert get_book_price("unknown_title") == 0

# Tests for calculate_discounted_price function
def test_calculate_discounted_price_valid_book_and_discount():
    """Test discounted price for an existing book with a valid discount percentage."""
    # 25.99 * (1 - 10/100) = 25.99 * 0.9 = 23.391
    assert calculate_discounted_price("python_guide", 10) == pytest.approx(23.391)
    # 32.50 * (1 - 25/100) = 32.50 * 0.75 = 24.375
    assert calculate_discounted_price("data_science", 25) == pytest.approx(24.375)

def test_calculate_discounted_price_valid_book_zero_discount():
    """Test discounted price with 0% discount, should be original price."""
    assert calculate_discounted_price("web_dev", 0) == pytest.approx(28.75)

def test_calculate_discounted_price_valid_book_full_discount():
    """Test discounted price with 100% discount, should be 0."""
    assert calculate_discounted_price("algorithms", 100) == pytest.approx(0.0)

def test_calculate_discounted_price_invalid_book():
    """Test discounted price for a non-existent book, should return 0."""
    assert calculate_discounted_price("non_existent_book", 10) == 0
    assert calculate_discounted_price("unknown_title", 50) == 0

def test_calculate_discounted_price_valid_book_over_100_percent_discount():
    """
    Test discounted price with a discount greater than 100%.
    Current implementation results in a negative price.
    """
    # 25.99 * (1 - 120/100) = 25.99 * (-0.2) = -5.198
    assert calculate_discounted_price("python_guide", 120) == pytest.approx(-5.198)

def test_calculate_discounted_price_valid_book_negative_discount():
    """
    Test discounted price with a negative discount (i.e., a markup).
    Current implementation increases the price.
    """
    # 25.99 * (1 - (-10)/100) = 25.99 * 1.1 = 28.589
    assert calculate_discounted_price("python_guide", -10) == pytest.approx(28.589)

# Tests for calculate_total_price function
def test_calculate_total_price_empty_list():
    """Test total price for an empty list of books."""
    assert calculate_total_price([]) == 0

def test_calculate_total_price_single_valid_book():
    """Test total price for a list containing a single valid book."""
    assert calculate_total_price(["python_guide"]) == pytest.approx(25.99)

def test_calculate_total_price_multiple_valid_books():
    """Test total price for a list containing multiple valid books."""
    # 25.99 + 32.50 = 58.49
    assert calculate_total_price(["python_guide", "data_science"]) == pytest.approx(58.49)
    # 25.99 + 32.50 + 28.75 = 87.24
    assert calculate_total_price(["python_guide", "data_science", "web_dev"]) == pytest.approx(87.24)

def test_calculate_total_price_single_invalid_book():
    """Test total price for a list containing a single non-existent book."""
    assert calculate_total_price(["non_existent_book"]) == 0

def test_calculate_total_price_mixed_books():
    """Test total price for a list containing both valid and invalid books."""
    # 25.99 (python_guide) + 0 (non_existent_book) + 28.75 (web_dev) = 54.74
    assert calculate_total_price(["python_guide", "non_existent_book", "web_dev"]) == pytest.approx(54.74)

def test_calculate_total_price_duplicate_books():
    """Test total price for a list containing duplicate books."""
    # 25.99 + 25.99 = 51.98
    assert calculate_total_price(["python_guide", "python_guide"]) == pytest.approx(51.98)

# Tests for combine_prices function
def test_combine_prices_two_valid_books():
    """Test combined price for two valid books with the bundle discount."""
    # (25.99 + 32.50) * 0.9 = 58.49 * 0.9 = 52.641
    assert combine_prices("python_guide", "data_science") == pytest.approx(52.641)
    # (28.75 + 45.00) * 0.9 = 73.75 * 0.9 = 66.375
    assert combine_prices("web_dev", "algorithms") == pytest.approx(66.375)

def test_combine_prices_first_book_invalid():
    """Test combined price when the first book is invalid (no discount)."""
    # 0 + 32.50 = 32.50 (no discount applied because one book is invalid)
    assert combine_prices("non_existent_book", "data_science") == pytest.approx(32.50)

def test_combine_prices_second_book_invalid():
    """Test combined price when the second book is invalid (no discount)."""
    # 25.99 + 0 = 25.99 (no discount applied because one book is invalid)
    assert combine_prices("python_guide", "non_existent_book") == pytest.approx(25.99)

def test_combine_prices_both_books_invalid():
    """Test combined price when both books are invalid."""
    assert combine_prices("non_existent_book1", "non_existent_book2") == 0

def test_combine_prices_same_book():
    """Test combined price when the same valid book is provided twice."""
    # (25.99 + 25.99) * 0.9 = 51.98 * 0.9 = 46.782
    assert combine_prices("python_guide", "python_guide") == pytest.approx(46.782)