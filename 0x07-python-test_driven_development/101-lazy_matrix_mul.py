import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        matrix_a = np.array(m_a, dtype=np.float64)
        matrix_b = np.array(m_b, dtype=np.float64)
        result = np.matmul(matrix_a, matrix_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    except Exception as e:
        raise TypeError(str(e)) from e
