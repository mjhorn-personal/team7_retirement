import pytest
from team7_retirement import FullRetirementAge, validations


'''
Example of a test I wrote. It tests the normal_retirement function 
in FullRetirementAge.py from team 7

If you run this test, you should see 2 tests passed. 

I test normal_retirement(1900, 1) and the way they wrote their function,
it should return a tuple with "65 and 0 months", 1965, and 1. 
It does, so the test passes. We need to write a test or parameter to test for
each boundary condition. So for exampmle, next we'd test for 1938, 1939 and so, on.
'''
@pytest.mark.parametrize("year,month,expected",
                         [(1900,1,("65 and 0 months", 1965, 1)),
                          (1937,2,("65 and 0 months", 2002, 2)),
                          (1938,3,("65 and 2 months", 2003, 5)),
                          (1939,4,("65 and 4 months", 2004, 8)),
                          (1940,5,("65 and 6 months", 2005, 11)),
                          (1941,6,("65 and 8 months", 2007, 2)),
                          (1942,7,("65 and 10 months", 2008, 5)),
                          (1943,8,("66 and 0 months", 2009, 8)),
                          (1954,9,("66 and 0 months", 2020, 9)),
                          (1955,10,("66 and 2 months", 2021, 12)),
                          (1956,11,("66 and 4 months", 2023, 3)),
                          (1957,12,("66 and 6 months", 2024, 6)),
                          (1958,1,("66 and 8 months", 2024, 9)),
                          (1959,2,("66 and 10 months", 2025, 12)),
                          (1960,3,("67 and 0 months", 2027, 3)),
                          (2999,4,("67 and 0 months", 3066, 4))])

def test_normal_retirement(year, month, expected):
    assert (FullRetirementAge.normal_retirement(year, month) ==
            expected)


'''
I have no idea how to test their validation because they have combined
input with validation!
'''
def test_validation_year_invalid_input():
 # code to test validation method
    pass


@pytest.mark.parametrize("month,expected", [(1, "January"),
                                            (2, "February"),
                                            (3, "March"),
                                            (4, "April"),
                                            (5, "May"),
                                            (6, "June"),
                                            (7, "July"),
                                            (8, "August"),
                                            (9, "September"),
                                            (10, "October"),
                                            (11, "November"),
                                            (12, "December")])
def test_month_to_string(month, expected):
    assert FullRetirementAge.month_string(month) == expected
