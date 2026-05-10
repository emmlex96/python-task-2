from palindrome_prime import is_palindrome

def test_is_palindrome():
    assert is_palindrome(2) == True
    assert is_palindrome(3) == True 
    assert is_palindrome(11) == True 
    assert is_palindrome(121) == False 
    assert is_palindrome(13) == False 
    assert is_palindrome(1) == False 
    assert is_palindrome(-11) == False 
    assert is_palindrome(0) == False 
    assert is_palindrome(101) == True
    assert is_palindrome(11.0) == False 
    print("All palindrome tests passed!")

test_is_palindrome()
