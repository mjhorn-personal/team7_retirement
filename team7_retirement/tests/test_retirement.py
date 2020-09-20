import pytest
from team7_retirement import FullRetirementAge



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
                          (1937,12,("65 and 0 months", 2002, 12))])
def test_normal_retirement_(year, month, expected):
    assert (FullRetirementAge.normal_retirement(year, month) ==
            expected)
