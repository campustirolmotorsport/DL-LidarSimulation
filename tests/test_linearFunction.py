import pytest
import numpy as np
from src.linearFunction import LinearFunction


def testLinearFunction():
    matrix = np.array([[1, 1], [5, 6]])
    f = LinearFunction(matrix)
    assert isinstance(f, LinearFunction)


def testAssertionLinearFunction():
    wrong_matrix = np.array([])
    with pytest.raises(AssertionError):
        LinearFunction(wrong_matrix)


def testSupportVector():
    supportVector = np.array([1, 2])
    directionVector = np.array([0, 0])
    matrix = np.array([supportVector, directionVector])
    f = LinearFunction(matrix)
    assert (supportVector == f.supportVector).all()


def testDirectionVector():
    supportVector = np.array([0, 0])
    directionVector = np.array([1, 2])
    matrix = np.array([supportVector, directionVector])
    f = LinearFunction(matrix)
    assert (directionVector == f.directionVetor).all()


def testSetterSupportVector():
    oldSupportVector = np.array([1, 2])
    newSupportVector = np.array([5, 1])
    matrix = np.array([oldSupportVector, np.array([0, 0])])
    f = LinearFunction(matrix)
    assert (oldSupportVector == f.supportVector).all()
    f.supportVector = newSupportVector
    assert (newSupportVector == f.supportVector).all()


def testSetterDirectionVector():
    oldDirectionVector = np.array([1, 2])
    newDirectionVector = np.array([5, 1])
    matrix = np.array([oldDirectionVector, np.array([0, 0])])
    f = LinearFunction(matrix)
    assert (oldDirectionVector == f.supportVector).all()
    f.supportVector = newDirectionVector
    assert (newDirectionVector == f.supportVector).all()


def testPointIsOnLine():
    point = (10, 5)
    matrix = np.array([[0, 0], [2, 1]])
    l = LinearFunction(matrix)
    assert l.onLine(point)


def testPointNotOnLine():
    point = (1, 5)
    matrix = np.array([[0, 0], [2, 1]])
    l = LinearFunction(matrix)
    assert not l.onLine(point)
