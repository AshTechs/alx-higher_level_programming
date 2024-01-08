#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b doesn't meet the requirements.
        ValueError: If m_a or m_b is empty or if matrices can't be multiplied.
    """
    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Check if elements in m_a and m_b are integers or floats
    for row in m_a:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b are rectangular matrices
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Convert lists to NumPy arrays and perform matrix multiplication
    result = np.dot(np.array(m_a), np.array(m_b))

    return result

