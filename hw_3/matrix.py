import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    @property
    def shape(self):
        return len(self.matrix), len(self.matrix[0])

    def _getcol(self, item):
        return [x[item] for x in self.matrix]

    def __str__(self):
        return (
            "["
            + "\n".join(
                [
                    "\t".join(["["] + [str(x) for x in self[i]] + ["]"])
                    for i in range(len(self))
                ]
            )
            + "]"
        )

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError(f"Invalid shapes")
        result = [[0] * self.shape[1] for _ in range(self.shape[0])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result[i][j] = self[i][j] + other[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError(f"Invalid shapes")
        result = [[0] * self.shape[1] for _ in range(self.shape[0])]
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                result[i][j] = self[i][j] * other[i][j]
        return Matrix(result)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError(f"Invalid shapes")
        result = [[0] * other.shape[1] for _ in range(self.shape[0])]
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                result[i][j] = sum([x * y for x, y in zip(self[i], other._getcol(j))])
        return Matrix(result)


np.random.seed(0)

m1 = Matrix(np.random.randint(0, 10, (10, 10)))
m2 = Matrix(np.random.randint(0, 10, (10, 10)))

with open("artifacts/3_1/matrix+.txt", "w") as f:
    res = m1 + m2
    f.write(str(res))

with open("artifacts/3_1/matrix*.txt", "w") as f:
    res = m1 * m2
    f.write(str(res))

with open("artifacts/3_1/matrix@.txt", "w") as f:
    res = m1 @ m2
    f.write(str(res))