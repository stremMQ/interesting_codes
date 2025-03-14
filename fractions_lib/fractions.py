class sumf:
    num1 = None
    den1 = None
    num2 = None
    den2 = None

    def __init__(self,num1,den1,num2,den2):

        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2

        self.suma()

    def suma(self):

        if type(self.num1) == int and type(self.den1) == int and type(self.num2) == int and type(self.den2) == int:

            if self.den1 != self.den2:

                self.den = self.den1 * self.den2
                self.num = self.num1 * self.den2 + self.num2 * self.den1

                MaxDel = 1

                if self.num == self.den:
                    rangeDel = self.num
                else:
                    rangeDel = min(self.num,self.den)

                for i in range(rangeDel, 1, -1):
                    if self.num % i == 0 and self.den % i == 0 and i > MaxDel:
                        MaxDel = i

                self.num /= MaxDel
                self.den /= MaxDel

            elif self.den1 == self.den2:

                self.num = self.num1 + self.num2

                MaxDel = 1

                for i in range(min(self.num,self.den2), 1, -1):
                    if self.num % i == 0 and self.den2 % i == 0 and i > MaxDel:
                        MaxDel = i

                self.den = self.den2

                self.num /= MaxDel
                self.den /= MaxDel

        else:

            print("ошибка")

    def __iter__(self):

        yield from (int(self.num), int(self.den))

class diff:
    num1 = None
    den1 = None
    num2 = None
    den2 = None

    def __init__(self, num1, den1, num2, den2):

        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2

        self.dif()

    def dif(self):

        if type(self.num1) == int and type(self.den1) == int and type(self.num2) == int and type(self.den2) == int:

            if self.den1 != self.den2:

                self.den = self.den1 * self.den2
                self.num = self.num1 * self.den2 - self.num2 * self.den1

                MaxDel = 1

                if self.num == self.den:
                    rangeDel = self.num
                else:
                    rangeDel = min(self.num, self.den)

                for i in range(rangeDel, 1, -1):
                    if self.num % i == 0 and self.den % i == 0 and i > MaxDel:
                        MaxDel = i

                self.num /= MaxDel
                self.den /= MaxDel

            elif self.den1 == self.den2:

                self.num = self.num1 - self.num2

                MaxDel = 1

                for i in range(min(self.num, self.den2), 1, -1):
                    if self.num % i == 0 and self.den2 % i == 0 and i > MaxDel:
                        MaxDel = i

                self.den = self.den2

                self.num /= MaxDel
                self.den /= MaxDel

        else:

            print("ошибка")

    def __iter__(self):

        yield from (int(self.num), int(self.den))

class timesf:
    num1 = None
    den1 = None
    num2 = None
    den2 = None

    def __init__(self, num1, den1, num2, den2):
        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2

        self.times()

    def times(self):
        if type(self.num1) == int and type(self.den1) == int and type(self.num2) == int and type(self.den2) == int:

            self.num = self.num1 * self.num2
            self.den = self.den1 * self.den2

            if self.num == self.den:
                rangeDel = self.num
            else:
                rangeDel = min(self.num,self.den)

            MaxDel = 1

            for i in range(rangeDel, 1, -1):
                if self.num % i == 0 and self.den % i == 0 and i > MaxDel:
                    MaxDel = i

            self.num /= MaxDel
            self.den /= MaxDel

        else:
            print("ошибка")

    def __iter__(self):
        yield from (int(self.num), int(self.den))

class sharef:
    num1 = None
    den1 = None
    num2 = None
    den2 = None

    def __init__(self, num1, den1, num2, den2):
        self.num1 = num1
        self.den1 = den1
        self.num2 = num2
        self.den2 = den2

        self.share()

    def share(self):
        if type(self.num1) == int and type(self.den1) == int and type(self.num2) == int and type(self.den2) == int:

            self.numr = self.den2
            self.denr = self.num2

            self.num = self.num1 * self.numr
            self.den = self.den1 * self.denr

            if self.num == self.den:
                rangeDel = self.num
            else:
                rangeDel = min(self.num,self.den)

            MaxDel = 1

            for i in range(rangeDel, 1, -1):
                if self.num % i == 0 and self.den % i == 0 and i > MaxDel:
                    MaxDel = i

            self.num /= MaxDel
            self.den /= MaxDel

        else:
            print("ошибка")


    def __iter__(self):
        yield from (int(self.num), int(self.den))