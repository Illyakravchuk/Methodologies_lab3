from fastapi import APIRouter
import numpy

router = APIRouter()


@router.get('/matrix')
def matrix() -> dict:
    matrix_a = numpy.random.rand(10, 10)
    matrix_b = numpy.random.rand(10, 10)
    product = numpy.dot(matrix_a, matrix_b)

    result = {
        "matrix_A": matrix_a.tolist(),
        "matrix_B": matrix_b.tolist(),
        "product of matrices": product.tolist()
    }

    return result
