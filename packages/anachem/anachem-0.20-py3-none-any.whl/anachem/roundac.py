from anachem import roundbase as roundbase
from anachem.roundbase import D
import math
from typing import Union


class AnaChemList(object):
    def __init__(self, data: list):
        if isinstance(data, AnaChemList):
            for attr in dir(data):
                if attr[:2] != '__':
                    setattr(self, attr, getattr(data, attr))
        else:
            # 数据,以列表形式存在
            self.data = data
            # 数据列表的形状,最大二维
            self.shape = None
            # 数据列表的元素类型,允许Decimal,Calc,(若为str,稍后会转换位Decimal)
            self.type = None

            # 计算形状
            shapelist = []
            counter1 = 0
            for i in self.data:
                if type(i) == list:
                    counter2 = 0
                    for j in i:
                        counter2 += 1
                    shapelist.append(counter2)
                counter1 += 1
            if len(shapelist) == 0:
                self.shape = [1, [counter1]]
            else:
                self.shape = [counter1, shapelist]

            # 格式化数据列表
            if self.shape[0] == 1:
                if isinstance(self.data[0], str) or isinstance(self.data[0], int):
                    new_data = []
                    for i in self.data:
                        new_data.append(D(i))
                    self.data = new_data
                    self.type = "D"
                elif isinstance(self.data[0], D):
                    self.type = "D"
                elif isinstance(self.data[0], roundbase.Calc):
                    self.type = "Calc"

            else:
                if isinstance(self.data[0][0], str) or isinstance(self.data[0][0], int):
                    new_data = []
                    counter = 0
                    for i in self.data:
                        new_data.append([])
                        for j in i:
                            new_data[counter].append(D(j))
                        counter += 1
                    self.data = new_data
                    self.type = "D"
                elif isinstance(self.data[0][0], D):
                    self.type = "D"
                elif isinstance(self.data[0][0], roundbase.Calc):
                    self.type = "Calc"

    # 生成未修约的列表
    def resultlist(self):
        if self.type == "D":
            return self.data

        elif self.type == "Calc":
            result_data = []
            if self.shape[0] == 1:
                for i in self.data:
                    result_data.append(i.result)
            else:
                counter = 0
                for i in self.data:
                    result_data.append([])
                    for j in i:
                        result_data[counter].append(j.result)
                    counter += 1
            return result_data

    # 生成修约后的列表
    def outputlist(self):
        if self.type == "D":
            return self.data

        elif self.type == "Calc":
            output_data = []
            if self.shape[0] == 1:
                for i in self.data:
                    output_data.append(i.output)
            else:
                counter = 0
                for i in self.data:
                    output_data.append([])
                    for j in i:
                        output_data[counter].append(j.output)
                    counter += 1
            return output_data

    def delete(self,order:list):
        pass

    def updateshape(self):
        shapelist = []
        counter1 = 0
        for i in self.data:
            if type(i) == list:
                counter2 = 0
                for j in i:
                    counter2 += 1
                shapelist.append(counter2)
            counter1 += 1
        if len(shapelist) == 0:
            self.shape = [1, [counter1]]
        else:
            self.shape = [counter1, shapelist]

    # 打印时,输出修约后的值组成的列表的str
    def __str__(self):
        return str(self.outputlist())


#  广播机制(条件:形状相同,某列表元素个数为1,某列表元素个数等于另一列表行数)
def broadcast(list1: AnaChemList, list2: AnaChemList, function, constant):
    resultlist = []

    # 如果形状相同
    if list1.shape == list2.shape:  # 如果形状相同
        if list1.shape[0] == 1:  # 如果形状相同且是一维列表
            for i in range(list1.shape[1][0]):  # i-->元素序号
                resultlist.append(eval(function)(list1.data[i], list2.data[i], constant))
        elif list1.shape[0] > 1:  # 如果形状相同且是二维列表
            for i in range(list1.shape[0]):  # i-->行号
                resultlist.append([])
                for j in range(list1.shape[1][i]):  # j-->第i行元素序号
                    resultlist[i].append(eval(function)(list1.data[i][j], list2.data[i][j], constant))

    # 列表1只有一个元素
    elif list1.shape[0] == 1 and list1.shape[1][0] == 1:  # 列表1只有一个元素
        num = list1.data[0]
        if list2.shape[0] == 1:  # 如果形状是一维列表
            for i in range(list2.shape[1][0]):  # i-->元素序号
                resultlist.append(eval(function)(num, list2.data[i], constant))
        elif list2.shape[0] > 1:  # 如果是二维列表
            for i in range(list2.shape[0]):  # i-->行号
                resultlist.append([])
                for j in range(list2.shape[1][i]):  # j-->第i行元素序号
                    resultlist[i].append(eval(function)(num, list2.data[i][j], constant))
    # 列表2只有一个元素
    elif list2.shape[0] == 1 and list2.shape[1][0] == 1:  # 列表2只有一个元素
        num = list2.data[0]
        if list1.shape[0] == 1:  # 如果形状是一维列表
            for i in range(list1.shape[1][0]):  # i-->元素序号
                resultlist.append(eval(function)(list1.data[i], num, constant))
        elif list1.shape[0] > 1:  # 如果是二维列表
            for i in range(list1.shape[0]):  # i-->行号
                resultlist.append([])
                for j in range(list1.shape[1][i]):  # j-->第i行元素序号
                    resultlist[i].append(eval(function)(list1.data[i][j], num, constant))

    # 列表1为二维列表,行数等于列表2行数,每行1个元素
    elif list1.shape[0] == list2.shape[0] and max(list1.shape[1]) == min(list1.shape[1]) == 1:
        if list2.shape[0] == 1:  # 如果形状是一维列表
            for i in range(list2.shape[1][0]):  # i-->元素序号
                resultlist.append(eval(function)(list1.data[0], list2.data[i], constant))
        elif list2.shape[0] > 1:  # 如果是二维列表
            for i in range(list2.shape[0]):  # i-->行号
                resultlist.append([])
                for j in range(list2.shape[1][i]):  # j-->第i行元素序号
                    resultlist[i].append(eval(function)(list1.data[i][0], list2.data[i][j], constant))
    # 列表2为二维列表,行数等于列表2行数,每行1个元素
    elif list2.shape[0] == list1.shape[0] and max(list2.shape[1]) == min(list2.shape[1]) == 1:
        if list1.shape[0] == 1:  # 如果形状是一维列表
            for i in range(list1.shape[1][0]):  # i-->元素序号
                resultlist.append(eval(function)(list1.data[i], list2.data[0], constant))
        elif list1.shape[0] > 1:  # 如果是二维列表
            for i in range(list1.shape[0]):  # i-->行号
                resultlist.append([])
                for j in range(list1.shape[1][i]):  # j-->第i行元素序号
                    resultlist[i].append(eval(function)(list1.data[i][j], list2.data[i][0], constant))

        # 列表1为一维列表,元素个数等于列表2行数
    elif list1.shape[0] == 1 and list1.shape[1][0] == list2.shape[0]:  # 列表1元素个数等于列表2行数
        if list2.shape[0] == 1:  # 如果形状是一维列表
            for i in range(list2.shape[1][0]):  # i-->元素序号
                resultlist.append(eval(function)(list1.data[0], list2.data[i], constant))
        elif list2.shape[0] > 1:  # 如果是二维列表
            for i in range(list2.shape[0]):  # i-->行号
                resultlist.append([])
                for j in range(list2.shape[1][i]):  # j-->第i行元素序号
                    resultlist[i].append(eval(function)(list1.data[i], list2.data[i][j], constant))
        # 列表2为一维列表,元素个数等于列表1行数
    elif list2.shape[0] == 1 and list2.shape[1][0] == list1.shape[0]:  # 列表2元素个数等于列表1行数
        if list1.shape[0] == 1:  # 如果形状是一维列表
            for i in range(list1.shape[1][0]):  # i-->元素序号
                resultlist.append(eval(function)(list1.data[i], list2.data[0], constant))
        elif list1.shape[0] > 1:  # 如果是二维列表
            for i in range(list1.shape[0]):  # i-->行号
                resultlist.append([])
                for j in range(list1.shape[1][i]):  # j-->第i行元素序号
                    resultlist[i].append(eval(function)(list1.data[i][j], list2.data[i], constant))

    resultlist = AnaChemList(resultlist)

    return resultlist


def add(num1: Union[D, roundbase.Calc, str, AnaChemList], num2: Union[D, roundbase.Calc, str, AnaChemList],
        constant: int = -1):
    if (isinstance(num1, D) or isinstance(num1, roundbase.Calc) or isinstance(num1, str)) \
            and (isinstance(num2, D) or isinstance(num2, roundbase.Calc) or isinstance(num2, str)):
        return roundbase.add(num1, num2, constant)
    elif isinstance(num1, AnaChemList) and isinstance(num2, AnaChemList):
        return broadcast(num1, num2, "roundbase.add", constant)


def subtract(num1: Union[D, roundbase.Calc, str, AnaChemList], num2: Union[D, roundbase.Calc, str, AnaChemList],
             constant: int = -1):
    if (isinstance(num1, D) or isinstance(num1, roundbase.Calc) or isinstance(num1, str)) \
            and (isinstance(num2, D) or isinstance(num2, roundbase.Calc) or isinstance(num2, str)):
        return roundbase.subtract(num1, num2, constant)
    elif isinstance(num1, AnaChemList):
        return broadcast(num1, num2, "roundbase.subtract", constant)


def multiply(num1: Union[D, roundbase.Calc, str, AnaChemList], num2: Union[D, roundbase.Calc, str, AnaChemList],
             constant: int = -1):
    if (isinstance(num1, D) or isinstance(num1, roundbase.Calc) or isinstance(num1, str)) \
            and (isinstance(num2, D) or isinstance(num2, roundbase.Calc) or isinstance(num2, str)):
        return roundbase.multiply(num1, num2, constant)
    elif isinstance(num1, AnaChemList):
        return broadcast(num1, num2, "roundbase.multiply", constant)


def divide(num1: Union[D, roundbase.Calc, str, AnaChemList], num2: Union[D, roundbase.Calc, str, AnaChemList],
           constant: int = -1):
    if (isinstance(num1, D) or isinstance(num1, roundbase.Calc) or isinstance(num1, str)) \
            and (isinstance(num2, D) or isinstance(num2, roundbase.Calc) or isinstance(num2, str)):
        return roundbase.divide(num1, num2, constant)
    elif isinstance(num1, AnaChemList):
        return broadcast(num1, num2, "roundbase.divide", constant)


def power(num1: Union[D, roundbase.Calc, str, AnaChemList], num2: Union[D, roundbase.Calc, str, AnaChemList],
          constant: int = 2):
    if (isinstance(num1, D) or isinstance(num1, roundbase.Calc) or isinstance(num1, str)) \
            and (isinstance(num2, D) or isinstance(num2, roundbase.Calc) or isinstance(num2, str)):
        return roundbase.divide(num1, num2, constant)
    elif isinstance(num1, AnaChemList):
        return broadcast(num1, num2, "roundbase.power", constant)


def log(num1: Union[D, roundbase.Calc, str, AnaChemList], num2: Union[D, roundbase.Calc, str, AnaChemList] = D(math.e),
        constant: int = 2):
    if (isinstance(num1, D) or isinstance(num1, roundbase.Calc) or isinstance(num1, str)) \
            and (isinstance(num2, D) or isinstance(num2, roundbase.Calc) or isinstance(num2, str)):
        return roundbase.log(num1, num2, constant)
    elif isinstance(num1, AnaChemList):
        num2 = AnaChemList([num2])
        return broadcast(num1, num2, "roundbase.log", constant)


def acsum(num1):
    if num1.shape[0] == 1:
        counter = 0
        for i in num1.data:
            if counter == 0:
                result = i
                counter += 1
            else:
                result = add(result, i)
                counter += 1

        return AnaChemList([result])

    else:
        counter1 = 0
        resultlist = []
        for i in num1.data:
            resultlist.append([])
            counter2 = 0
            for j in i:
                if counter2 == 0:
                    result = j
                    counter2 += 1
                else:
                    result = add(result, j)
                    counter2 += 1
            resultlist[counter1].append(result)
            counter1 += 1
        resultlist = AnaChemList(resultlist)

        return resultlist


def absolute(num1):
    new_num1 = []
    if num1.type == "D":
        if num1.shape[0] == 1:
            for i in num1.data:
                new_num1.append(abs(i))
        else:
            counter = 0
            for i in num1.data:
                new_num1.append([])
                for j in i:
                    new_num1[counter].append(abs(j))
                counter += 1

    elif num1.type == "Calc":

        if num1.shape[0] == 1:
            for i in num1.data:
                if i.result < 0:
                    new_num1.append(subtract(D('0'), i, 1))
                else:
                    new_num1.append(i)

        else:
            counter = 0
            for i in num1.data:
                new_num1.append([])
                for j in i:
                    if j.result < 0:
                        new_num1[counter].append(subtract(D('0'), j, 1))
                    else:
                        new_num1[counter].append(j)
                counter += 1

        new_num1 = AnaChemList(new_num1)

        return new_num1


# 求极值辅助函数
def max_index(list):
    max = list[0]
    index = 0
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
            index = i
    return index


def min_index(list):
    min = list[0]
    index = 0
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
            index = i
    return index


def second_max_index(list):
    max = list[0]
    index_max = 0

    second_max = list[0]
    index_second_max = 0

    for i in range(len(list)):

        if list[i] > max:
            second_max = max
            index_second_max = index_max

            max = list[i]
            index_max = i

        elif list[i] > second_max:
            second_max = list[i]
            index_second_max = i

    return index_second_max


def second_min_index(list):
    min = list[0]
    index_min = 0

    second_min = list[0]
    index_second_min = 0

    for i in range(len(list)):

        if list[i] < min:
            second_min = min
            index_second_min = index_min

            min = list[i]
            index_min = i

        elif list[i] < second_min:
            second_min = list[i]
            index_second_min = i

    return index_second_min


def peak(num1, function):
    if num1.shape[0] == 1:

        index = eval(function)(num1.resultlist())
        peak_value = num1.data[index]

        return AnaChemList([peak_value]), [index]

    else:
        counter1 = 0
        peak_value_list = []
        peak_index_list = []
        for i in num1.resultlist():
            peak_value_list.append([])
            peak_index_list.append([])
            index = eval(function)(i)
            peak_value = num1.data[counter1][index]

            peak_value_list[counter1].append(peak_value)
            peak_index_list[counter1].append(index)
            counter1 += 1

        return AnaChemList(peak_value_list), peak_index_list


# 求极值
def first_max(num1):
    return peak(num1, "max_index")


def first_min(num1):
    return peak(num1, "min_index")


def second_max(num1):
    return peak(num1, "second_max_index")


def second_min(num1):
    return peak(num1, "second_min_index")


# 统计
def acrange(num1):
    return subtract(first_max(num1)[0], first_min(num1)[0])


def number(num1):
    return AnaChemList(num1.shape[1])


def mean(num1):
    sum_data = acsum(num1)
    mean_data = divide(sum_data, number(num1), 2)
    return mean_data


# 与error有关

# 　多　误差
def error(num1, true_value):
    return subtract(num1, true_value)


# 　多　相对误差
def relative_error(num1, true_value, _error=None):
    if _error is None:
        return multiply(divide(error(num1, true_value), true_value), AnaChemList(['100']), 2)
    else:
        return multiply(divide(_error, true_value), AnaChemList(['100']), 2)


# 1 标准偏差
def standard_deviation(num1, true_value, _error=None):
    if _error is None:
        a = acsum(power(error(num1, true_value), AnaChemList(['2']), 2))
        a = power(divide(a, number(num1), 2), AnaChemList(["0.5"]), 2)
    else:
        a = acsum(power(_error, AnaChemList(['2']), 2))
        a = power(divide(a, number(num1), 2), AnaChemList(["0.5"]), 2)
    return a


# 与deviation有关

# 多 偏差
def deviation(num1, _mean=None):
    if _mean is None:
        return subtract(num1, mean(num1))
    else:
        return subtract(num1, _mean)


# 多 相对偏差
def relative_deviation(num1, _deviation=None, _mean=None):
    if _mean is None:
        _mean = mean(num1)
    if _deviation is None:
        _deviation = deviation(num1, _mean)
    return multiply(divide(_deviation, _mean), AnaChemList(['100']), 2)


# 1 平均偏差
def average_deviation(num1, _deviation=None, _mean=None):
    if _deviation is None:
        if _mean is None:
            _mean = mean(num1)
        _deviation = deviation(num1, _mean)
    return divide((acsum(absolute(_deviation))), number(num1), 2)


# 1 相对平均偏差
def relative_average_deviation(num1, _average_deviation=None, _deviation=None, _mean=None):
    if _mean is None:
        _mean = mean(num1)
    if _average_deviation is None:
        if _deviation is None:
            _deviation = deviation(num1, _mean)
        _average_deviation = average_deviation(num1, _deviation, _mean)
    return multiply(divide(_average_deviation, _mean), AnaChemList(['100']), 2)


# 1 样本标准偏差 自由度N-1
def sample_standard_deviation(num1, _deviation=None, _mean=None):
    if _deviation is None:
        if _mean is None:
            _mean = mean(num1)
        _deviation = deviation(num1, _mean)
    a = acsum(power(_deviation, AnaChemList(['2']), 2))
    b = subtract(number(num1), AnaChemList(['1']), 2)
    a = power(divide(a, b, 2), AnaChemList(["0.5"]), 2)
    return a


# 1 相对标准偏差 自由度N-1
def relative_standard_deviation(num1, _sample_standard_deviation=None, _deviation=None, _mean=None):
    if _mean is None:
        _mean = mean(num1)
    if _sample_standard_deviation is None:
        if _deviation is None:
            _deviation = deviation(num1, _mean)
        _sample_standard_deviation = sample_standard_deviation(num1, _deviation, _mean)
    return divide(_sample_standard_deviation, _mean)


# 1 变异系数
def coefficient_of_variation(num1, _relative_standard_deviation=None, _sample_standard_deviation=None, _deviation=None,
                             _mean=None):
    if _relative_standard_deviation is None:
        if _mean is None:
            _mean = mean(num1)
        if _sample_standard_deviation is None:
            if _deviation is None:
                _deviation = deviation(num1, _mean)
            _sample_standard_deviation = sample_standard_deviation(num1, _deviation, _mean)
        _relative_standard_deviation = relative_standard_deviation(num1, _mean=_mean,
                                                                   _sample_standard_deviation=_sample_standard_deviation)
    return multiply(_relative_standard_deviation, AnaChemList(['100']), 2)


# 1 重复性
def repeatability(num1, _coefficient_of_variation=None, _relative_standard_deviation=None,
                  _sample_standard_deviation=None, _deviation=None, _mean=None):
    if _coefficient_of_variation is None:
        if _relative_standard_deviation is None:
            if _mean is None:
                _mean = mean(num1)
            if _sample_standard_deviation is None:
                if _deviation is None:
                    _deviation = deviation(num1, _mean)
                _sample_standard_deviation = sample_standard_deviation(num1, _deviation, _mean)
            _relative_standard_deviation = relative_standard_deviation(num1, _mean=_mean,
                                                                       _sample_standard_deviation=_sample_standard_deviation)
        _coefficient_of_variation = coefficient_of_variation(num1,
                                                             _relative_standard_deviation=_relative_standard_deviation)
    return multiply(_coefficient_of_variation, AnaChemList([D(math.sqrt(2) * 2)]), 2)


if __name__ == "__main__":
    a1 = AnaChemList([['0.2862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863'],
                      ['0.2862', '0.2859', '0.2851', '0.2848', '0.2852']])
    c2 = AnaChemList(['12', '12.1', '13.2', '11', '13.2'])
    print(coefficient_of_variation(a1), relative_standard_deviation(a1), sample_standard_deviation(a1),
          relative_average_deviation(a1))
    print(average_deviation(a1), relative_deviation(a1))
    # print(first_max(a1),first_min(a1))
    print(first_max(a1)[0], first_min(a1)[0], second_min(a1))
    print(acrange(a1))
    # print(acsum(a1), a1.shape)
    # print(mean(a1))
    # print(acsum(c2).resultlist(), c2.shape)
    # print(mean(c2).resultlist())
    # print(error(a1,AnaChemList(['0.2862','0.2862'])))
    # a = relative_error(a1, AnaChemList(['0.2862', '0.2862']))
    # b = average_deviation(a)
    # c = E()
    # print(c)
    # print(a)
    # print(b.resultlist(),b)
    # print(standard_deviation(a1, AnaChemList(['0.2862', '0.2862'])))

    # print(a1.shape, a1.data)
    # b1 = AnaChemList(['0.2862', '0.2859', 0.2851, 0.2848, 0.2852, 0.2863])
    # print(b1.shape, b1.data)
    # c1 = toDecimal([['0.2862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863'],
    #                ['0.2862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863']])
    # print(c1)

    # a2 = AnaChemList([['0.2862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863'],
    #                  ['0.2862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863']])
    # b2 = AnaChemList([['0.2862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863'],
    #                  ['0.2862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863']])
    # d2 = AnaChemList([["1.0000"], ["2.000"]])
    # d3 = AnaChemList([["10"], ["2"]])
    # c2 = broadcast(b2, d2, 1)
    # c3 = broadcast(d2, b2, 1)
    # print(c2)
    # print(c3)
    # c4 = broadcast(a2,b2,"roundbase.add")
    # print(c4)
    # add(1,1,1)
    # print(power(a2, d3))
    # print(add(D("0.92"), D("0.523")))
    # print(log(b2, D("10")))
    # a2 = AnaChemList([['0.2862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863'],
    #                   ['0.2862', '0.2859', '0.2851', '0.2848', '0.2452', '0.2863']])
    # b2 = AnaChemList(['0.2862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863'])
    # t1=add(a2,a2)
    # print(t1)
    # print(statistics.mean(a2.data))
    # c=sum(a2)
    # b = sum(b2)
    # print(sum(a2),a2.shape,c.data)
    # print(type(sum(b2)), b2.shape, b.output,b.result)
    # print(fist_max(c2), sum(c2).result, second_max(c2))
    # print(sum(t1))
    # print(second_max(t1))
