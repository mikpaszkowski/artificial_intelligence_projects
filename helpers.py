import numpy

from enums import MethodType


def function_F_derivative(coeff, x):
    return 3 * coeff.a * x ** 2 + 2 * coeff.b * x + coeff.c


def function_F(coeff, x):
    return coeff.a * x ** 3 + coeff.b * x ** 2 + coeff.c * x + coeff.d


def derivative_G(coeff, x):
    return numpy.dot(2, numpy.dot(coeff.A, x)) + coeff.b


def function_G(coeff, x):
    return numpy.dot(numpy.transpose(x), numpy.dot(coeff.A, x)) + numpy.dot(numpy.transpose(coeff.b),
                                                                            x) + coeff.c


def getGradientValue_F(method, coeff, x):
    if method == MethodType.GRADIENT_DESCENT:
        return function_F_derivative(coeff, x)
    else:
        return (function_F_derivative(coeff, x)) / (
                6 * coeff.a * x + 2 * coeff.b)


def getGradientValue_G(method, coeff, x):
    if method == MethodType.GRADIENT_DESCENT:
        return derivative_G(coeff, x)
    else:
        return numpy.divide(function_G(coeff, x),
                            derivative_G(coeff, x))
