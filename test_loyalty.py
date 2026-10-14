import pytest
from loyalty import loyalty_points


def test_guest_19_uah_gets_zero_points():
    amount, is_member = 19, False
    result = loyalty_points(amount, is_member)
    assert result == 0


def test_guest_20_uah_gets_one_point():
    amount, is_member = 20, False
    result = loyalty_points(amount, is_member)
    assert result == 1


def test_member_40_uah_gets_four_points():
    amount, is_member = 40, True
    result = loyalty_points(amount, is_member)
    assert result == 4


def test_zero_amount_gets_zero_points():
    amount, is_member = 0, False
    result = loyalty_points(amount, is_member)
    assert result == 0


def test_negative_amount_raises_error():
    amount, is_member = -1, False
    with pytest.raises(ValueError):
        loyalty_points(amount, is_member)


def test_member_boundary_39_uah_gets_two_points():
    amount, is_member = 39, True
    result = loyalty_points(amount, is_member)
    assert result == 2


def test_member_100_uah_gets_ten_points():
    amount, is_member = 100, True
    result = loyalty_points(amount, is_member)
    assert result == 10
