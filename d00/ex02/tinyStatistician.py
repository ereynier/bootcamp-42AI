import math

class TinyStatistician():
    def __init__(self):
        pass

    def mean(self,x):
        out = 0.0
        if (len(x) == 0):
            return
        for i in range(len(x)):
            out += float(x[i])
        return (float(out / len(x)))

    def median(self,x):
        out = 0.0
        if (len(x) == 0):
            return
        if ((len(x) % 2) != 0):
            out = float(x[len(x) / 2])
        else:
            out = float((x[((len(x)) / 2)] + x[(len(x) / 2) - 1]))
            out = out / 2
        return (out)

    def quartile(self, x, percentile):
        out = 0.0
        percentile = float(percentile) / 100
        if (len(x) == 0):
            return
        n = float((len(x) + 1) * percentile) - 1
        if (n % 1 == 0):
            n = int(n)
            return (float(x[n]))
        else:
            n = int(n)
            return (float((x[n] + x[n + 1])) / 2)

    def var(self, x):
        out = 0.0
        if (len(x) == 0):
            return
        for i in range(len(x)):
            out += (float(x[i]) - self.mean(x))**2
        out = out / len(x)
        return (out)

    def std(self, x):
        out = 0.0
        if (len(x) == 0):
            return
        return(math.sqrt(self.var(x)))