#!/usr/bin/python3
"""
Module
"""


def lazy_matrix_mul(m_a, m_b):
    """function return matrix multiplication with Numpy

    Args:
        m_a: matrix a
        m_b: matrix b
    Return:
        m_a * m_b
    """
    import numpy as np
    return (np.dot(m_a, m_b))
