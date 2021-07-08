from os import name
from second_min import find_second_min


def test1():
    arr = [11,10,1,9,4,12,1,8,2]
    try:
        assert find_second_min(arr) == 2, "Should be 4"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')

def test2():
    arr = [9,4,12,1,8,2]
    try:
        assert find_second_min(arr) == 4, "Should be 2"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test3():
    arr = [101,12543,99,1075,311147,647,101]
    try:
        assert find_second_min(arr) == 101, "Should be 101"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test4():
    arr = [4,1,2,9,7,6,4,1,2,8]
    try:
        assert find_second_min(arr) == 2, "Should be 2"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')

def test5():
    arr = [8,6]
    try:
        assert find_second_min(arr) == 8, "Should be 8"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')

def test6():
    arr = [400,850,765,125,731,359]
    try:
        assert find_second_min(arr) == 359, "Should be 359"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test7():
    arr = [400,850,765,125,731,359]
    try:
        assert find_second_min(arr) == 400, "Should be 359"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test8():
    arr = [1,2,3,4,5,6,7,8,9,0]
    try:
        assert find_second_min(arr) == 1, "Should be 1"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test9():
    arr = [9,11,13,15,13,11,9]
    try:
        assert find_second_min(arr) == 11, "Should be 11"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test10():
    arr = [985010231,84468030,1234640,9794316,5661313]
    try:
        assert find_second_min(arr) == 5661313, "Should be 5661313"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')

if __name__ == "__main__":
    number_of_tests = 10
    for i in range(1,number_of_tests+1):
        test_name = 'test' + str(i)
        print(test_name, end =" ")
        eval(test_name + '()')
    
    
