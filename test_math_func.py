import pytest
import math_func
import sys


@pytest.mark.parametrize('num1,num2,result',
                            [
                                (7,3,10),
                                ('Hello',' World','Hello World'),
                                (10.5,25.5,36)
                            ])
def test_add(num1,num2,result):
        assert math_func.add(num1,num2) == result

    # assert math_func.add(7,3) == 10
    # result = math_func.add('Hello', ' wolrd')
    # assert result == 'Hello World'
    # result = math_func.add(10.5, 25.5)
    # assert result == 36




# #@pytest.mark.number
# def test_product():
#     assert math_func.product(5,5) ==25
#     assert math_func.product(5) == 10
#     assert math_func.product(6) == 12
#
#
# #@pytest.mark.strings
# def test_add_string():
#     result = math_func.add('Hello ','World')
#     assert result == 'Hello World'
#     assert type(result) is str
#     assert 'Hello' in result
#
#
# #@pytest.mark.strings
# def test_product_string():
#     assert math_func.product('Hello ',3) == 'Hello Hello Hello '
#     result = math_func.product('Hello' )
#     assert result == 'HelloHello'
#     assert type(result) is str
#     assert 'Hello' in result