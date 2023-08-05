from decimal import Decimal, ROUND_HALF_EVEN
import math
from typing import Union

"""
 创建运算器对象
 单次加减乘除返回修约后数据,将未修约数据及指导修约的指令保存到对象属性中
 再次加减乘除使用未修约数据保运算,指导修约的指令保存到对象属性中
"""

D = Decimal


# 该类为加减乘除等运算的父类,提供公共方法
class Calc(object):

    def __init__(self):
        # 运算完成后以下属性均会被填充

        # 修约后的值
        self.output = None
        # 未修约的原始值
        self.result = None
        # 用于指导修约的有效数值位数
        self.SignificantDigits = None
        # 用于指导修约的指数(小数点对于有效数字的位移)
        self.exponent = None

    # Decimal-->有效数字位数
    def getSignificantDigits(self, num: Decimal):
        significantDigits = len(num.as_tuple().digits)
        return significantDigits

    # Decimal-->指数
    def getExponent(self, num: Decimal):
        afterPoint = num.as_tuple().exponent
        return afterPoint

    # Decimal,指定位数-->保留小数点后指定位数
    def byPrecision(self, num: Decimal, precision):
        result = num.quantize(Decimal('0.'+('0'*(precision-1))+'1'), ROUND_HALF_EVEN)
        return result

    # 运算后的结果Decimal,参与运算的数的指数--根据指数修约-->(修约后的数值,起作用的指数)
    def byExponent(self, result: Decimal, exponent1, exponent2, constant: int):
        if constant == -1:
            exponent = max(exponent1, exponent2)
        elif constant == 1:
            exponent = exponent2
        elif constant == 2:
            exponent = exponent1

        result = result.quantize(Decimal('1e' + str(exponent)), ROUND_HALF_EVEN)

        return result, exponent

    # 运算后的结果Decimal,参与运算的数的有效数字位数--根据有效数字位数修约-->(修约后的数值,起作用的有效数字位数)
    def bysignificantDigits(self, result: Decimal, SignificantDigits1, SignificantDigits2, constant: int):

        if constant == -1:
            significantDigits = min(SignificantDigits1, SignificantDigits2)
        elif constant == 1:
            significantDigits = SignificantDigits2
        elif constant == 2:
            significantDigits = SignificantDigits1

        if result != 0:
            operationValue = math.floor(math.log10(abs(result)))+1-significantDigits
        else:
            operationValue = 0
        result = result.quantize(Decimal('1e' + str(operationValue)), ROUND_HALF_EVEN)

        return result, significantDigits

    # 打印时,输出修约后的值
    def __str__(self):
        return str(self.output)


# 数1和数2允许的类型:Decimal, Calc, str--运算-->修约后的值,未修约的原始值,用于指导修约的有效数值位数,用于指导修约的指数

# 加法运算
class add(Calc):
    def __init__(self, num1: Union[Decimal, Calc, str], num2: Union[Decimal, Calc, str], constant: int = -1, precision=None):
        super().__init__()
        if isinstance(num1, str):
            num1 = D(num1)
        if isinstance(num2, str):
            num2 = D(num2)

        if isinstance(num1, Calc):
            exponent1 = num1.exponent
            num1 = num1.result
        else:
            exponent1 = self.getExponent(num1)

        if isinstance(num2, Calc):
            exponent2 = num2.exponent
            num2 = num2.result
        else:
            exponent2 = self.getExponent(num2)

        self.result = num1 + num2

        self.output, self.exponent = self.byExponent(self.result, exponent1, exponent2, constant)

        self.SignificantDigits = self.getSignificantDigits(self.output)

        if precision is not None:
            self.output = self.byPrecision(self.result, precision)


# 减法运算
class subtract(Calc):
    def __init__(self, num1: Union[Decimal, Calc, str], num2: Union[Decimal, Calc, str], constant: int = -1, precision=None):
        super().__init__()
        if isinstance(num1, str):
            num1 = D(num1)
        if isinstance(num2, str):
            num2 = D(num2)

        if isinstance(num1, Calc):
            exponent1 = num1.exponent
            num1 = num1.result
        else:
            exponent1 = self.getExponent(num1)

        if isinstance(num2, Calc):
            exponent2 = num2.exponent
            num2 = num2.result
        else:
            exponent2 = self.getExponent(num2)

        self.result = num1 - num2

        self.output, self.exponent = self.byExponent(self.result, exponent1, exponent2, constant)

        self.SignificantDigits = self.getSignificantDigits(self.output)

        if precision is not None:
            self.output = self.byPrecision(self.result, precision)


# 乘法运算
class multiply(Calc):
    def __init__(self, num1: Union[Decimal, Calc, str], num2: Union[Decimal, Calc, str], constant: int = -1, precision=None):
        super().__init__()

        if isinstance(num1, str):
            num1 = D(num1)
        if isinstance(num2, str):
            num2 = D(num2)

        if isinstance(num1, Calc):
            SignificantDigits1 = num1.SignificantDigits
            num1 = num1.result
        else:
            SignificantDigits1 = self.getSignificantDigits(num1)

        if isinstance(num2, Calc):
            SignificantDigits2 = num2.SignificantDigits
            num2 = num2.result
        else:
            SignificantDigits2 = self.getSignificantDigits(num2)

        self.result = num1 * num2

        self.output, self.SignificantDigits = self.bysignificantDigits(self.result, SignificantDigits1, SignificantDigits2, constant)

        self.exponent = self.getExponent(self.output)

        if precision is not None:
            self.output = self.byPrecision(self.result, precision)


# 除法运算
class divide(Calc):
    def __init__(self, num1: Union[Decimal, Calc, str], num2: Union[Decimal, Calc, str], constant: int = -1, precision=None):
        super().__init__()

        if isinstance(num1, str):
            num1 = D(num1)
        if isinstance(num2, str):
            num2 = D(num2)

        if isinstance(num1, Calc):
            SignificantDigits1 = num1.SignificantDigits
            num1 = num1.result
        else:
            SignificantDigits1 = self.getSignificantDigits(num1)

        if isinstance(num2, Calc):
            SignificantDigits2 = num2.SignificantDigits
            num2 = num2.result
        else:
            SignificantDigits2 = self.getSignificantDigits(num2)

        self.result = num1 / num2

        self.output, self.SignificantDigits = self.bysignificantDigits(self.result, SignificantDigits1,
                                                                       SignificantDigits2, constant)

        self.exponent = self.getExponent(self.output)

        if precision is not None:
            self.output = self.byPrecision(self.result, precision)


# 幂运算
class power(Calc):
    def __init__(self, num1: Union[Decimal, Calc, str], num2: Union[Decimal, Calc, str], constant: int = 2, precision=None):
        super().__init__()

        if isinstance(num1, str):
            num1 = D(num1)
        if isinstance(num2, str):
            num2 = D(num2)

        if isinstance(num1, Calc):
            SignificantDigits1 = num1.SignificantDigits
            num1 = num1.result
        else:
            SignificantDigits1 = self.getSignificantDigits(num1)

        if isinstance(num2, Calc):
            SignificantDigits2 = num2.SignificantDigits
            num2 = num2.result
        else:
            SignificantDigits2 = self.getSignificantDigits(num2)

        self.result = num1 ** num2

        self.output, self.SignificantDigits = self.bysignificantDigits(self.result, SignificantDigits1,
                                                                       SignificantDigits2, 2)

        self.exponent = self.getExponent(self.output)

        if precision is not None:
            self.output = self.byPrecision(self.result, precision)


# 对数运算
class log(Calc):
    def __init__(self, num1: Union[Decimal, Calc, str], num2: Union[Decimal, Calc, str] = D(math.e), constant=2, precision=None):
        super().__init__()

        if isinstance(num1, str):
            num1 = D(num1)
        if isinstance(num2, str):
            num2 = D(num2)

        if isinstance(num1, Calc):
            self.SignificantDigits = num1.SignificantDigits
            num1 = num1.result
        else:
            self.SignificantDigits = self.getSignificantDigits(num1)

        if isinstance(num2, Calc):
            num2 = num2.result

        self.result = D(math.log(num1, num2))

        self.output = self.result.quantize(Decimal('1e-' + str(self.SignificantDigits)), ROUND_HALF_EVEN)

        self.exponent = self.getExponent(self.output)

        if precision is not None:
            self.output = self.byPrecision(self.result, precision)


if __name__ == "__main__":
    # 测试用例
    a = add(D("0.335"), D("0.45"))
    b = add(D("0.3"), a)
    print(a)
    print(b)
    print(a.output,a.result,a.exponent)
    print(b.output, b.result, b.exponent)
    c = subtract(D("0.335"), D("0.45"))
    d = subtract(c, b,precision=3)
    print(c)
    print(d)
    print(c.output,c.result,c.exponent)
    print(d.output, d.result, d.exponent)
    a1 = multiply(D("2278"), D("0.123"))
    a2 = multiply(a1, D("0.12"))
    a3 = multiply(a1, a2)
    print(a1, a2, a3)
    print(a1.result,a2.result,a3.result)
    a1 = divide(D("2278"), D("0.123"))
    a2 = divide(a1, D("0.12"))
    a3 = divide(a1, a2)
    print(a1, a2, a3)
    print(a1.result,a2.result,a3.result)
    a1 = power(D("2"), D("10"))
    a2 = power(a1, D("0.5"))
    a3 = power(a1, a2)
    print(a1, a2, a3)
    print(a1.result, a2.result, a3.result)
    a1 = log(D("0.675e10"))
    a2 = log(a1, D("0.5"))
    a3 = log(a1, D("10"))
    print(a1, a2, a3)
    print(a1.result, a2.result, a3.result)
    a2 = multiply(D("0.234"), D("23.23"))
    a3 = divide(D("0.6"), D("0.78"))
    a1 = add(a2, a3)
    a4 = multiply(a1,D("0.321"))
    print(a1, a2, a3, a4)
    print(a1.result, a2.result, a3.result,a4.result)
    a = divide(multiply(multiply(D("0.0325"), D("5.104")), D("60.094")), D("139.56"))
    a = add(log(D("23.121e3")), D("9.02"))
    print(a, a.result)
    print(log(D("23.121e3")))
