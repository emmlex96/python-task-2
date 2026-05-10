from apply_discount import apply_discount

def test_apply_discount():
    assert apply_discount("Shoes", 100, "SAVE10") == 90.0, "Test 1 Failed"
    assert apply_discount("Bag", 200, "HALFOFF") == 100.0, "Test 2 Failed"
    assert apply_discount("Hat", 50, "INVALIDCODE") == 50.0, "Test 3 Failed"
    assert apply_discount("Shirt", 80) == 80.0, "Test 4 Failed"
    assert apply_discount("Free item", 0, "SAVE10") == 0.0, "Test 5 Failed"
    try:
        apply_discount("Ghost item", -50, "SAVE10")
        assert False, "Test 6 Failed"
    except ValueError:
        pass
    assert apply_discount("Book", 19.99, "SAVE10") == 17.99, "Test 7 Failed"
    print("All apply_discount tests passed!")

test_apply_discount()
