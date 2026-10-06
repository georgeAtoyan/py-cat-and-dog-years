from app.main import get_human_age


def test_zero_cat_and_dog_year() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_15_cat_and_dog_years_give_0_human_year() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_first_15_cat_and_dog_years_give_1_human_year() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_23_cat_and_dog_years_give_1_human_year() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_next_9_cat_and_dog_years_give_1_human_year() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_cat_and_dog_years_have_different_conversion_rates() -> None:
    assert get_human_age(24, 29) == [2, 3]


def test_cat_27_years_and_dog_28_years_give_2_human_age() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_next_4_cat_and_5_dog_years_give_1_human_year() -> None:
    assert get_human_age(28, 29) == [3, 3]
