# Given 2 matrices with dimensions x and y, return the sum of the matrices
def matrix_addition(x, y):
    return [[x[i][j] + y[i][j] for j in range(len(x[i]))] for i in range(len(x))]


# Given 2 matrices with dimensions x and y, return the difference of the matrices
def matrix_subtraction(x, y):
    return [[x[i][j] - y[i][j] for j in range(len(x[i]))] for i in range(len(x))]


# Given 2 matrices with dimensions x and y, return the product of the matrices
def matrix_multiplication(x, y):
    return [
        [sum(x[i][k] * y[k][j] for k in range(len(x))) for j in range(len(y[0]))]
        for i in range(len(x))
    ]


# Given a matrix with dimensions x and y, return the determinant of the matrix
def matrix_determinant(x):
    if len(x) == 1:
        return x[0][0]
    else:
        return sum(
            x[0][i]
            * matrix_determinant(
                matrix_subtraction(x[1:], [[x[0][j]] for j in range(len(x[0]))])
            )
            * (-1) ** i
            for i in range(len(x[0]))
        )


# Given a matrix with dimensions x and y, return the inverse of the matrix
def matrix_inverse(x):
    det = matrix_determinant(x)
    if det == 0:
        return None
    else:
        return [
            [
                matrix_determinant(
                    matrix_subtraction(x, [[x[0][j]] for j in range(len(x[0]))])
                )
                * (-1) ** i
                for i in range(len(x[0]))
            ]
            for j in range(len(x))
        ]


# Given a matrix with dimensions x and y, return the cofactor of the matrix
def matrix_cofactor(x):
    return [
        [
            matrix_determinant(
                matrix_subtraction(x, [[x[0][j]] for j in range(len(x[0]))])
            )
            * (-1) ** i
            for i in range(len(x[0]))
        ]
        for j in range(len(x))
    ]
