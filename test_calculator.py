import calculator

def test_add_postive_numbers():
    assert calculator.add(6, 7) == 13

def test_add_negative_numbers():
    assert calculator.add(-6, -7) == -13

def test_add_float_postive_numbers():
    assert calculator.add(6.7, 4.1) == 10.8

def test_add_float_negative_numebers():
    assert calculator.add(-6.7, -4.1) == -10.8

def test_subtract_postive_numbers():
    assert calculator.subtract (10, 6) == 4

def test_subtract_negative_numbers():
    assert calculator.subtract(-10, -6) == -4

def test_subtract_postive_float_numbers():
    assert calculator.subtract(3.5, 2.5) == 1

def test_subtract_negative_float_numbers():
    assert calculator.subtract(-3.5, -2.5) == -1

def test_multiply_postive_numbers():
    assert calculator.multiply(2, 2) == 4

def test_multiply_negative_numbers():
    assert calculator.multiply(-4, -2) == 8

def test_multiply_float_positive_numbers():
    assert calculator.multiply(1.1, 4.4) == 4.84

def test_multiply_float_negative_numbers():
    assert calculator.multiply(-1.1, -4.4) == 4.84

def test_divide_postive_numbers():
    assert calculator.divide(10, 2) == 5

def test_divide_negative_numbers():
    assert calculator.divide(-10, -2) == 5

def test_divide_float_positve_numbers():
    assert calculator.divide(10.5, 2.5) == 4.2

def test_divide_float_negative_numbers():
    assert calculator.divide(-10.5, -2.5) == 4.2

