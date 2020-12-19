from vector import Vector


class Matrix:
    def __init__(self, *args):
        err = 0
        self.data = []
        self.shape = (0, 0)
        if (len(args) == 1):
            if isinstance(args[0], list):
                self.data = args[0]
                size = len(self.data[0])
                for i in self.data:
                    if (not isinstance(i, list) or len(i) != size or err):
                        print("not a list of 'float list', with same size")
                        err = 1
                        break
                    else:
                        for j in i:
                            if not isinstance(j, (float, int)):
                                err = 1
                                break
                self.shape = (len(self.data), len(self.data[0]))
            if isinstance(args[0], tuple) and len(args[0]) == 2:
                self.shape = args[0]
                for i in range(self.shape[0]):
                    self.data.append([])
                    for j in range(self.shape[1]):
                        self.data[i].append(0)
        if (len(args) == 2):
            if (not isinstance(args[0], list)
                    or not isinstance(args[1], tuple)):
                err = 1
            else:
                self.data = args[0]
                self.shape = args[1]
                if (len(self.data) != self.shape[1]):
                    err = 1
                else:
                    for i in self.data:
                        if (len(self.data[i]) != self.shape[2]):
                            err = 1
        if (err):
            self.data = []
            self.shape = (0, 0)

    def T(self):
        out = []
        for i in range(self.shape[1]):
            out.append([])
            for j in range(self.shape[0]):
                out[i].append(self.data[j][i])
        return Matrix(out)

    def __add__(self, rhs):
        out = []
        if isinstance(rhs, Vector):
            if (rhs.size != self.shape[0]):
                print("Vector and matrice are not the same size")
                return (Matrix(0))
            else:
                for i in range(self.shape[0]):
                    out.append([])
                    for j in range(self.shape[1]):
                        out[i].append(self.data[i][j] + rhs.values[i])
        elif isinstance(rhs, Matrix):
            if (rhs.shape[0] != self.shape[0]
                    or rhs.shape[1] != self.shape[1]):
                print("Matrices are not the same shape")
                return (Matrix(0))
            else:
                for i in range(self.shape[0]):
                    out.append([])
                    for j in range(self.shape[1]):
                        out[i].append(self.data[i][j] + rhs.data[i][j])
        return (Matrix(out))

    def __radd__(self, rhs):
        return(self.__add__(rhs))

    def __sub__(self, rhs):
        out = []
        if isinstance(rhs, Vector):
            if (rhs.size != self.shape[0]):
                print("Vector and matrice are not the same size")
                return (Matrix(0))
            else:
                for i in range(self.shape[0]):
                    out.append([])
                    for j in range(self.shape[1]):
                        out[i].append(self.data[i][j] - rhs.values[i])
        elif isinstance(rhs, Matrix):
            if (rhs.shape[0] != self.shape[0]
                    or rhs.shape[1] != self.shape[1]):
                print("Matrices are not the same shape")
                return (Matrix(0))
            else:
                for i in range(self.shape[0]):
                    out.append([])
                    for j in range(self.shape[1]):
                        out[i].append(self.data[i][j] - rhs.values[i][j])
        return (Matrix(out))

    def __rsub__(self, rhs):
        out = []
        if isinstance(rhs, Vector):
            if (rhs.size != self.shape[0]):
                print("Vector and matrice are not the same size")
                return (Matrix(0))
            else:
                for i in range(self.shape[0]):
                    out.append([])
                    for j in range(self.shape[1]):
                        out[i].append(rhs.values[i] - self.data[i][j])
        elif isinstance(rhs, Matrix):
            if (rhs.shape[0] != self.shape[0]
                    or rhs.shape[1] != self.shape[1]):
                print("Matrices are not the same shape")
                return (Matrix(0))
            else:
                for i in range(self.shape[0]):
                    out.append([])
                    for j in range(self.shape[1]):
                        out[i].append(rhs.values[i][j] - self.data[i][j])
        return (Matrix(out))

    def __truediv__(self, rhs):
        out = []
        if isinstance(rhs, (float, int)):
            if (rhs == 0):
                print("ERROR: division by 0")
                return (Matrix(0))
            for i in range(self.shape[0]):
                out.append([])
                for j in range(self.shape[1]):
                    out[i].append(self.data[i][j] / rhs)
        return (Matrix(out))

    def __rtruediv__(self, rhs):
        out = []
        if isinstance(rhs, (float, int)):
            for i in range(self.shape[0]):
                out.append([])
                for j in range(self.shape[1]):
                    if (self.data[i][j] == 0):
                        print("ERROR: division by 0")
                        return (Matrix(0))
                    out[i].append(rhs / self.data[i][j])
        return (Matrix(out))

    def __mul__(self, rhs):
        out = []
        sum = 0
        if isinstance(rhs, Vector):
            if (rhs.size != self.shape[1]):
                print("Vector and matrice are not the same size")
                return (Matrix(0))
            else:
                for i in range(self.shape[0]):
                    sum = 0
                    for j in range(self.shape[1]):
                        sum += self.data[i][j] * rhs.values[i]
                    out[0].append(sum)
                    return (Vector(out))
        elif isinstance(rhs, Matrix):
            if (self.shape[1] != rhs.shape[0]):
                print("Matrices are not compatible")
                return (Matrix(0))
            else:
                for i in range(self.shape[0]):
                    for j in range(rhs.shape[1]):
                        sum = 0
                        for k in range(rhs.shape[0]):
                            sum += self.data[i][k] * rhs.data[k][j]
                        out.append(sum)
                return (Vector(out))
        if isinstance(rhs, (float, int)):
            for i in range(self.shape[0]):
                out.append([])
                for j in range(self.shape[1]):
                    out[i].append(self.data[i][j] * rhs)
        return (Matrix(out))

    def __rmul__(self, rhs):
        out = []
        sum = 0
        if isinstance(rhs, Vector):
            if (rhs.size != self.shape[1]):
                print("Vector and matrice are not the same size")
                return (Matrix(0))
            else:
                for i in range(self.shape[0]):
                    sum = 0
                    for j in range(self.shape[1]):
                        sum += self.data[i][j] * rhs.values[i]
                    out[0].append(sum)
                    return (Vector(out))
        elif isinstance(rhs, Matrix):
            if (self.shape[0] != rhs.shape[1]):
                print("Matrices are not compatible")
                return (Matrix(0))
            else:
                for i in range(rhs.shape[0]):
                    for j in range(self.shape[1]):
                        sum = 0
                        for k in range(self.shape[0]):
                            sum += rhs.data[i][k] * self.data[k][j]
                        out.append(sum)
                return (Vector(out))
        if isinstance(rhs, (float, int)):
            for i in range(self.shape[0]):
                out.append([])
                for j in range(self.shape[1]):
                    out[i].append(self.data[i][j] * rhs)
        return (Matrix(out))

    def __str__(self):
        return ("Matrix: {} shape: {}".format(self.data, self.shape))

    def __repr__(self):
        return (self.data)