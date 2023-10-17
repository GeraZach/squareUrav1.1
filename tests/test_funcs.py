from functions import *


def test_discriminant():
    assert discriminant(1,1,1) == -3
    assert discriminant(1e4, 1e4, 1e4) == -300000000
    assert discriminant(1e-4, 1e-4, 1e-4) == -3.0000000000000004e-08

    assert discriminant(1,2,1) == 0
    assert discriminant(1e4, 2e4, 1e4) == 0
    assert discriminant(1e-4, 2e-4, 1e-4) == 0

    assert discriminant(1,4,1) == 12
    assert discriminant(1e4, 4e4, 1e4) == 1200000000
    assert discriminant(1e-4, 4e-4, 1e-4) == 1.2000000000000002e-07

    #Дописать для inf и nan


def test_calculate_roots():
    assert calculate_roots(1,1,1, -3) == (-0.49999999999999994+0.8660254037844386j, -0.5-0.8660254037844386j)
    assert calculate_roots(1.0, 2.0, 3.0, -8.0) == (-0.9999999999999999+1.4142135623730951j, -1-1.4142135623730951j)
    assert calculate_roots(100.0 , 25.0 , 7678.0 , -3070575.0) == (-0.12499999999999947+8.761528120139774j, -0.12500000000000053-8.761528120139774j)
    assert calculate_roots(-456.0 , -234.0 , float('inf') , float('inf')) == (float('-inf'), float('inf'))


def test_fix_output_imaginary():
    assert fix_output_imaginary('(2+4j)', '(-3-5j)') == ('2+4i', '-3-5i')
    assert fix_output_imaginary('()()()()()', 'jjjjjj') == ('', 'iiiiii')


def test_a_is_zero():
    assert a_is_zero(1,1) == -1.0
    assert a_is_zero(2, 4) == -2.0
    assert a_is_zero(-1, 1) == 1.0
    assert a_is_zero(-2, 4) == 2.0
    assert a_is_zero(0.1,0.1) == -1.0
    assert a_is_zero(-0.1, 0.1) == 1.0


def test_coefficients_zero_check():
    assert coefficients_zero_check(0,1,1) == -1.0
    assert coefficients_zero_check(0,0,1) == noRootsOutput
    assert coefficients_zero_check(0,0,0) == infiniteRootsOutput
    assert coefficients_zero_check(1,0,1) == fullEquation


def test_discriminant_equals_zero():
    assert discriminant_equals_zero(1,2) == (-1.0, -1.0)
    assert discriminant_equals_zero(5,3 ) == (-0.3, -0.3)
    assert discriminant_equals_zero(100,250) == (-1.25, -1.25)


def test_solve_equation():

    #Whole numbers
    assert solve_equation(1,1,1) == ('-0.49999999999999994+0.8660254037844386i', '-0.5-0.8660254037844386i')
    assert solve_equation(1,1,0) == ('0.0', '-1.0')
    assert solve_equation(1,0,0) == (0.0, 0.0)
    assert solve_equation(0,0,0) == 'Бесконечное число решений'
    assert solve_equation(1,0,1) == ('6.123233995736766e-17+1i', '-6.123233995736766e-17-1i')
    assert solve_equation(0,0,1) == 'Нет корней'
    assert solve_equation(0,1,1) == -1.0
    assert solve_equation(0,1,0) == 0.0

    #Fractional numbers
    assert solve_equation(0.1,0.1,0.1) == ('-0.49999999999999994+0.8660254037844387i', '-0.5000000000000001-0.8660254037844387i')
    assert solve_equation(.1,.1,.1) == ('-0.49999999999999994+0.8660254037844387i', '-0.5000000000000001-0.8660254037844387i')
    assert solve_equation(1.0,1.0,1.0) == ('-0.49999999999999994+0.8660254037844386i', '-0.5-0.8660254037844386i')
    assert solve_equation(-0.1, -0.1, -0.1) == ('-0.5000000000000001-0.8660254037844387i', '-0.49999999999999994+0.8660254037844387i')
    assert solve_equation(-.1, -.1, -.1) == ('-0.5000000000000001-0.8660254037844387i', '-0.49999999999999994+0.8660254037844387i')
    assert solve_equation(-1.0, -1.0, -1.0) == ('-0.5-0.8660254037844386i', '-0.49999999999999994+0.8660254037844386i')

    #With exponent
    assert solve_equation(float('1e100'), float('1e-100'),  float('1.1e100')) == ('6.422101994144992e-17+1.0488088481701514i', '-6.422101994144992e-17-1.0488088481701514i')
    assert solve_equation(float('1.1e-100'), float('-1e100'), float('-1.1e-100')) == ('9.090909090909092e+199', '0.0')
    assert solve_equation(float('-1.1e100'), float('-1.1e-100'), 1) == ('-9.534625892455923e-51', '9.534625892455923e-51')

    #Infinity and NaN check
    assert solve_equation(float('inf'), float('inf'), float('inf')) == None
    assert solve_equation(float('-inf'), float('-inf'), float('-inf')) == None
    assert solve_equation(float('+inf'), float('-inf'), float('+inf')) == None
    assert solve_equation(float('nan'), float('nan'), float('nan')) == None



