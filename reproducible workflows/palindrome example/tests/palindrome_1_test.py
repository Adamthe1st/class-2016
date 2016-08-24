from palindrome import is_palindrome

def test_single_character():
    assert is_palindrome("a") == True
    
def test_two_same_character():
    assert is_palindrome("bb")==True
    
def test_numbers_not_palindrome():
    assert is_palindrome("ab3d")==False
    
def test_spacing_palindrome():
    assert is_palindrome("  kayak")==True
    
def test_capitals_palindrome():
    assert is_palindrome(" Noon   ")==True
    
def test_punctuation_palindrome():
    assert is_palindrome("\"Sirrah! Deliver deified desserts detartrated!\" stressed deified, reviled Harris.")==True