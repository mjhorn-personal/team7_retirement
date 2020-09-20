import pytest



'''
# test calculate_retirement_age:
@pytest.mark.parametrize("year", ['d', 'zero', '-8', '#', '[](*6+'])
def test_calculate_retirement_age_letters_non_numeric(year):
    with pytest.raises(ValueError):
        calculate_retirement_age(year)


@pytest.mark.parametrize("year", [-1, 0, 1899, 3000])
def test_calculate_retirement_age_invalid_year(year):
    with pytest.raises(ValueError):
        calculate_retirement_age(year)


@pytest.mark.parametrize("year", [1900, 1937])
def test_calculate_retirement_age_65year0mo(year):
    value = calculate_retirement_age(year)
    assert value == (65, 0)


@pytest.mark.parametrize("year", [1938])
def test_calculate_retirement_age_65year2mo(year):
    value = calculate_retirement_age(year)
    assert value == (65, 2)


@pytest.mark.parametrize("year", [1939])
def test_calculate_retirement_age_65year4mo(year):
    value = calculate_retirement_age(year)
    assert value == (65, 4)


@pytest.mark.parametrize("year", [1940])
def test_calculate_retirement_age_65year6mo(year):
    value = calculate_retirement_age(year)
    assert value == (65, 6)


@pytest.mark.parametrize("year", [1941])
def test_calculate_retirement_age_65year8mo(year):
    value = calculate_retirement_age(year)
    assert value == (65, 8)


@pytest.mark.parametrize("year", [1942])
def test_calculate_retirement_age_65year10mo(year):
    value = calculate_retirement_age(year)
    assert value == (65, 10)


@pytest.mark.parametrize("year", [1943, 1954])
def test_calculate_retirement_age_66year0mo(year):
    value = calculate_retirement_age(year)
    assert value == (66, 0)


@pytest.mark.parametrize("year", [1955])
def test_calculate_retirement_age_66year2mo(year):
    value = calculate_retirement_age(year)
    assert value == (66, 2)


@pytest.mark.parametrize("year", [1956])
def test_calculate_retirement_age_66year4mo(year):
    value = calculate_retirement_age(year)
    assert value == (66, 4)


@pytest.mark.parametrize("year", [1957])
def test_calculate_retirement_age_66year6mo(year):
    value = calculate_retirement_age(year)
    assert value == (66, 6)


@pytest.mark.parametrize("year", [1958])
def test_calculate_retirement_age_66year8mo(year):
    value = calculate_retirement_age(year)
    assert value == (66, 8)


@pytest.mark.parametrize("year", [1959])
def test_calculate_retirement_age_66year10mo(year):
    value = calculate_retirement_age(year)
    assert value == (66, 10)


@pytest.mark.parametrize("year", [1960, 2999])
def test_calculate_retirement_age_67year0mo(year):
    value = calculate_retirement_age(year)
    assert value == (67, 0)


# test calculate_retirement_date(birth_year, birth_month, age_years, age_months)
# "Constants"
VALID_BIRTH_YEAR = 1945
VALID_BIRTH_MONTH = 4
VALID_AGE_YEAR = 66
VALID_AGE_MONTH = 0


@pytest.mark.parametrize("birth_year", [-1, 0, 1899, 3000, 'year', '&*#-'])
def test_calculate_retirement_date_invalid_birth_year(birth_year):
    with pytest.raises(ValueError):
        calculate_retirement_date(birth_year, VALID_BIRTH_MONTH,
                                  VALID_AGE_YEAR, VALID_AGE_MONTH)


@pytest.mark.parametrize("birth_month", [-1, 0, 13, 'month', '&*#-'])
def test_calculate_retirement_date_invalid_birth_month(birth_month):
    with pytest.raises(ValueError):
        calculate_retirement_date(VALID_BIRTH_YEAR, birth_month,
                                  VALID_AGE_YEAR, VALID_AGE_MONTH)


@pytest.mark.parametrize("age_year", [-1, 0, 64, 68, 'year', '*&#)@'])
def test_calculate_retirement_date_invalid_age_year(age_year):
    with pytest.raises(ValueError):
        calculate_retirement_date(VALID_BIRTH_YEAR, VALID_BIRTH_MONTH,
                                  age_year, VALID_AGE_MONTH)


@pytest.mark.parametrize("age_month", [-1, 12, 'month', '$#@#'])
def test_calculate_retirement_date_invalid_age_month(age_month):
    with pytest.raises(ValueError):
        calculate_retirement_date(VALID_BIRTH_YEAR, VALID_BIRTH_MONTH,
                                  VALID_AGE_YEAR, age_month)


def test_calculate_retirement_date_valid_date():
    value = calculate_retirement_date(VALID_BIRTH_YEAR, VALID_BIRTH_MONTH,
                                      VALID_AGE_YEAR, VALID_AGE_MONTH)
    assert value == (2011, 4)
'''