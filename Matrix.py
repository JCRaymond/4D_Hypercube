from numbers import Number

class Matrix:

    def __init__(self, arg0, N = None, fill = 0):
        self.rows = None
        self.cols = None
        self.vals = None
        if type(arg0) is list:
            self.rows = len(list(arg0))
            self.cols = len(list(arg0)[0])
            for row in arg0:
                if len(row) != self.cols:
                    raise ValueError("Not all rows have the same number of columns")
            self.vals = arg0
        else:
            self.rows = arg0
            self.cols = N
            self.vals = [[fill for col in range(self.cols)] for row in range(self.rows)]

    @staticmethod
    def identity(n):
        m = Matrix(n, n)
        for i in range(n):
            m[i][i] = 1
        return m

    def transpose(self):
        m = Matrix(self.cols, self.rows)
        for r in range(self.rows):
            for c in range(self.cols):
                m[c][r] = self[r][c]
        return m

    def homogeneous(self):
        m = self.copy()
        m.vals.append([1 for col in range(m.cols)])
        m.rows += 1
        return m

    def copy(self):
        m = Matrix(self.rows, self.cols)
        for r in range(self.rows):
            for c in range(self.cols):
                m[r][c] = self[r][c]
        return m

    def __get_longest_elem_len(self):
        longest = 0
        for row in self:
            for elem in row:
                if len(str(elem)) > longest:
                    longest = len(str(elem))
        return longest

    def __str__(self):
        elemlen = self.__get_longest_elem_len()
        ret = ""
        for row in self:
            for elem in row:
                ret += str(elem).rjust(elemlen) + " "
            ret += "\n"
        return ret

    def __iter__(self):
        return iter(self.vals)

    def __neg__(self):
        return -1*self.copy()

    def __getitem__(self, item):
        return self.vals[item]

    def __setitem__(self, key, value):
        if len(list(value)) != self.cols:
            raise ValueError("The row you are setting must be of size: " + self.cols)

        self[key] = list(value)

    def __mul__(self, other):
        if not isinstance(other, (Matrix, Number)):
            raise TypeError("You must multiply by a number or anoter Matrix.")

        m = None

        if isinstance(other, Number):
            m = self.copy()
            for r in range(self.rows):
                for c in range(self.cols):
                    m[r][c] *= other

        else:
            if self.cols != other.rows:
                raise ValueError("The number of rows in the rows in the first Matrix must equal the number of columns in the second")

            m = Matrix(self.rows, other.cols)
            other_t = other.transpose()
            for r, row in enumerate(self):
                for c, col in enumerate(other_t):
                    m[r][c] = sum([rval*cval for rval, cval in zip(row, col)])

        return m

    def __rmul__(self, other):
        if not isinstance(other, Number):
            TypeError("Invalid")
        return self*other