class Vector:
    def __init__(self, arg):
        self.shape = (0,0)
        self.values = []
        self.row = False
        self.size = 0
        if isinstance(arg, list):
            if all(isinstance(x, float) for x in arg):
                self.shape = (1, len(arg))
                self.row = True
                self.values = arg
            elif all(isinstance(x, list) for x in arg):
                for x in arg:
                    if all(isinstance(y, float) for y in x):
                        self.shape = (len(arg), 1)
                        self.values = arg
        elif isinstance(arg, int):
            self.shape = (arg, 1)
            for i in range(0, self.shape[0]):
                self.values.append([float(i)])
#        elif isinstance(arg, range):
#            self.shape = (abs(arg.stop - arg.start), 1)
#            for i in arg:
#               self.values.append([float(i)])
        elif (isinstance(arg, tuple) and len(arg) == 2):
            flag = 1
            for i in arg:
                if not isinstance(i, int):
                    flag = 0
            if (flag):
                self.size = abs(arg[0] - arg[1])
                self.shape = (self.size, 1)
                for i in range(0, self.size):
                    self.values.append([float(i + arg[0])])
        if (self.row == False):
            self.size = self.shape[0]
        else:
            self.size = self.shape[1]
            
    def T(self):
        out = []
        if (self.row == False):
            self.row = True
            for i in range(0, self.size):
                out.append(self.values[i][0])
        else:
            self.row = False
            for i in rang(0, self.size):
                out.append(self.values[i])
        return(Vector(out))

    def dot(self, rhs):
        out = 0
        if (isinstance(rhs, Vector)):
            if (self.shape != rhs.shape):
                print("vectors haven't the same shape")
                return (0)
            if (self.row == False):
                for i in range(0, self.size):
                    out += self.values[i][0] * rhs.values[i][0]
            else:
                for i in range(0, self.size):
                    out += self.values[i] * rhs.values[i]
        else:
            print("not a vector")
        return (out)


    def __add__(self, rhs):
        out = []
        if (isinstance(rhs, Vector)):
            if (self.shape != rhs.shape):
                print("vectors haven't the same shape")
                return (Vector(0))
            for i in range(0, self.shape):
                out.append(self.values[i] + rhs.values[i])
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.shape):
                out.append(self.values[i] + rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __radd__(self, rhs):
        out = []
        if (isinstance(rhs, Vector)):
            if (self.shape != rhs.shape):
                print("vectors haven't the same shape")
                return (Vector(0))
            for i in range(0, self.size):
                out.append(self.values[i] + rhs.values[i])
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] + rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __sub__(self, rhs):
        out = []
        if (isinstance(rhs, Vector)):
            if (self.shape != rhs.shape):
                print("vectors haven't the same shape")
                return (Vector(0))
            for i in range(0, self.size):
                out.append(self.values[i] - rhs.values[i])
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] - rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __rsub__(self, rhs):
        out = []
        if (isinstance(rhs, Vector)):
            if (self.shape != rhs.shape):
                print("vectors haven't the same size")
                return (Vector(0))
            for i in range(0, self.size):
                out.append(rhs.values[i] - self.values[i])
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(rhs - self.values[i])
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __truediv__(self, rhs):
        out = []
        if (rhs == 0):
            print("div by 0 impossible")
            return (Vector(0))
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] / rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __rtruediv__(self, rhs):
        out = []
        if (rhs == 0):
            print("div by 0 impossible")
            return (Vector(0))
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                if (self.values[i] == 0):
                    print("div by 0 impossible")
                    return (Vector(0))
                out.append(rhs / self.values[i])
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __mul__(self, rhs):
        out = []
        x = 0
        if (isinstance(rhs, Vector)):
            if (self.shape != rhs.shape):
                print("vectors haven't the same shape")
                return (Vector(0))
            for i in range(0, self.size):
                x += self.values[i] * rhs.values[i]
                return (x)
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] * rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __rmul__(self, rhs):
        out = []
        x = 0
        if (isinstance(rhs, Vector)):
            if (self.shape != rhs.shape):
                print("vectors haven't the same shape")
                return (Vector(0))
            for i in range(0, self.size):
                x += self.values[i] * rhs.values[i]
                return (x)
        elif (isinstance(rhs, int) or isinstance(rhs, float)):
            for i in range(0, self.size):
                out.append(self.values[i] * rhs)
        else:
            print("ERROR: problem to adding {} to vector".format(rhs))
            return (Vector(0))
        return (Vector(out))

    def __str__(self):
        return ("vector: {} shape: {}".format(self.values, self.shape))

    def __repr__(self):
        return (self.values)