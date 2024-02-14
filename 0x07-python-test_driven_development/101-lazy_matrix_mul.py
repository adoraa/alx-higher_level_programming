#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using NumPy.

    Args:
    - m_a (list of lists): First matrix.
    - m_b (list of lists): Second matrix.

    Returns:
    - New matrix as a result of the multiplication.

    Raises:
    - ValueError: If matrices cannot be multiplied.
    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result.tolist()
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
