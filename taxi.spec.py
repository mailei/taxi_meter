from Meter import Meter


def test_validate():
    assert Meter.is_validate(1), "Should be True"
    assert not Meter.is_validate(0), "Should be False"
    assert not Meter.is_validate(-1), "Should be False"
    print("validate test passed")


def test_calc():
    assert Meter.calc_price(2000) == 1200, "Should be 1200"
    assert Meter.calc_price(500) == 600, "Should be 600"
    assert Meter.calc_price(5000) == 3000, "Should be 3000"
    print("calc test passed")


if __name__ == "__main__":
    test_validate()
    test_calc()
    print("all test passed")
