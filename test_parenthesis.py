from os import name
from parenthesis import open_close_parenthesis


def test1():
    phrase = '(Hello (World))'
    try:
        assert open_close_parenthesis(phrase) == True, "Should be True"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')

def test2():
    phrase = '(Hello) (World)'
    try:
        assert open_close_parenthesis(phrase) == True, "Should be True"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test3():
    phrase = '(Hello(World))'
    try:
        assert open_close_parenthesis(phrase) == False, "Should be True"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test4():
    phrase = '(Hello World)This is a Test)'
    try:
        assert open_close_parenthesis(phrase) == False, "Should be False"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')

def test5():
    phrase = 'This is (a) Test(Hello World))'
    try:
        assert open_close_parenthesis(phrase) == False, "Should be False"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')

def test6():
    phrase = 'This (is ((a) Test)(Hello World))'
    try:
        assert open_close_parenthesis(phrase) == False, "Should be True"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test7():
    phrase = 'This (is) ((a)) Test)('
    try:
        assert open_close_parenthesis(phrase) == False, "Should be False"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test8():
    phrase = '()(()))'
    try:
        assert open_close_parenthesis(phrase) == False, "Should be False"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test9():
    phrase = '(((())))'
    try:
        assert open_close_parenthesis(phrase) == True, "Should be True"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')


def test10():
    phrase = '()(()))()'
    try:
        assert open_close_parenthesis(phrase) == True, "Should be False"
        print(f'passed')
    except AssertionError as err:
        print(f'Failed - Assertion Error: {err}')

if __name__ == "__main__":
    number_of_tests = 10
    for i in range(1,number_of_tests+1):
        test_name = 'test' + str(i)
        print(test_name, end =" ")
        eval(test_name + '()')
    
    
