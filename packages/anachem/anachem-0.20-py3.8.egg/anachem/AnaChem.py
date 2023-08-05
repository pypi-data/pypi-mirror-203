from anachem.roundbase import D
from anachem import roundac as roundac
import copy


# Q表,G表,t表
Q_table = [[D('3'),  D('0.94'), D('0.98'), D('0.99')],
           [D('4'),  D('0.76'), D('0.85'), D('0.93')],
           [D('5'),  D('0.64'), D('0.73'), D('0.82')],
           [D('6'),  D('0.56'), D('0.64'), D('0.74')],
           [D('7'),  D('0.51'), D('0.59'), D('0.68')],
           [D('8'),  D('0.47'), D('0.54'), D('0.63')],
           [D('9'),  D('0.44'), D('0.51'), D('0.60')],
           [D('10'), D('0.41'), D('0.48'), D('0.57')]]

G_table = [[D('3'),  D('1.15'), D('1.15'), D('1.15')],
           [D('4'),  D('1.46'), D('1.48'), D('1.49')],
           [D('5'),  D('1.67'), D('1.71'), D('1.75')],
           [D('6'),  D('1.82'), D('1.89'), D('1.94')],
           [D('7'),  D('1.94'), D('2.02'), D('2.10')],
           [D('8'),  D('2.03'), D('2.13'), D('2.22')],
           [D('9'),  D('2.11'), D('2.21'), D('2.32')],
           [D('10'), D('2.18'), D('2.29'), D('2.41')],
           [D('11'), D('2.23'), D('2.36'), D('2.48')],
           [D('12'), D('2.29'), D('2.41'), D('2.55')],
           [D('13'), D('2.33'), D('2.46'), D('2.61')],
           [D('14'), D('2.37'), D('2.51'), D('2.66')],
           [D('15'), D('2.41'), D('2.55'), D('2.71')]]

t_table = [[D('2'),  D('6.314'), D('12.706'), D('63.657')],
           [D('3'),  D('2.920'), D('4.303'),  D('9.925')],
           [D('4'),  D('2.353'), D('3.182'),  D('5.841')],
           [D('5'),  D('2.132'), D('2.776'),  D('4.604')],
           [D('6'),  D('2.015'), D('2.571'),  D('4.032')],
           [D('7'),  D('1.943'), D('2.447'),  D('3.707')],
           [D('8'),  D('1.895'), D('2.365'),  D('3.500')],
           [D('9'),  D('1.860'), D('2.306'),  D('3.355')],
           [D('10'), D('1.833'), D('2.262'),  D('3.250')],
           [D('11'), D('1.812'), D('2.228'),  D('3.169')]]


class AnaChem(roundac.AnaChemList):
    # 初始化
    def __init__(self, data: roundac.AnaChemList, true_value=None, confidence_level_interval=None,
                 discard_suspicious=False, discard_method="Grubbs", confidence_discard=None):
        """

        :param data:
        :param true_value:
        :param confidence_level_interval:
        :param discard_suspicious:
        :param discard_method:
        :param confidence_discard:
        """
        super().__init__(data)
        self.aclist = data
        self.aclist_copy = copy.deepcopy(data)

        self.true_value = true_value
        self.confidence_level_interval = confidence_level_interval
        self.sort = sort
        self.discard_suspicious = discard_suspicious
        self.discard_method = discard_method
        self.confidence_discard = confidence_discard

        if discard_suspicious:
            self.discard(discard_method=discard_method, confidence_discard=confidence_discard, renovate=False)

        self.statistics()

    # 计算统计值
    def statistics(self):
        self.number = roundac.number(self.aclist)
        self.mean = roundac.mean(self.aclist)
        self.deviation = roundac.deviation(self.aclist)
        self.relative_deviation = roundac.relative_deviation(self.aclist)
        self.average_deviation = roundac.average_deviation(self.aclist)
        self.relative_average_deviation = roundac.relative_average_deviation(self.aclist)
        self.sample_standard_deviation = roundac.sample_standard_deviation(self.aclist)
        self.relative_standard_deviation = roundac.relative_standard_deviation(self.aclist)
        self.coefficient_of_variation = roundac.coefficient_of_variation(self.aclist)
        self.repeatability = roundac.repeatability(self.aclist)

        if self.true_value is not None:
            self.error = roundac.error(self.aclist, self.true_value)
            self.relative_error = roundac.relative_error(self.aclist, self.true_value)
            self.standard_deviation = roundac.standard_deviation(self.aclist, self.true_value)

        self.confidence_interval = self.confidence_interval_i(self.confidence_level_interval)

    # 舍去离群点
    def discard(self, discard_method="Grubbs", confidence_discard=None, renovate=True):
        """

        :param discard_method:
        :param confidence_discard:
        :param renovate:
        :return:
        """
        discard_data = []
        number = roundac.number(self.aclist)
        shape = self.shape

        # Grubbs法
        if discard_method == "Grubbs":
            # 计算G计算
            mean = roundac.mean(self.aclist)
            sample_standard_deviation = roundac.sample_standard_deviation(self.aclist)
            minlist = roundac.first_min(self.aclist)[0]
            maxlist = roundac.first_max(self.aclist)[0]
            grubbs1 = roundac.divide(roundac.subtract(mean, minlist), sample_standard_deviation)
            grubbs2 = roundac.divide(roundac.subtract(maxlist, mean), sample_standard_deviation)

            # 获取G表
            if confidence_discard is None:
                self.confidence_discard = 0.95
                row = 1  # 0.95
            if confidence_discard == 0.95:
                row = 1
            elif confidence_discard == 0.975:
                row = 2
            elif confidence_discard == 0.99:
                row = 3
            else:
                row = 1

            # print("bug",minlist,maxlist,discard_data)
            # G计算与G表比较
            if shape[0] == 1:
                rank = int(number.data[0])
                G_t = G_table[rank - 3][row]
                # print("初始",self.aclist)
                if grubbs1.resultlist()[0] > G_t:
                    self.data.remove(minlist.data[0])
                    discard_data.append(minlist.data[0])
                if grubbs2.resultlist()[0] > G_t:
                    self.data.remove(maxlist.data[0])
                    discard_data.append(maxlist.data[0])
            else:
                for i in range(shape[0]):
                    discard_data.append([])
                    rank = int(number.data[i])
                    G_t = G_table[rank - 3][row]
                    # print(i,grubbs1.resultlist()[i][0],grubbs2.resultlist()[i][0],G_t)
                    if grubbs1.resultlist()[i][0] > G_t:
                        self.data[i].remove(minlist.data[i][0])
                        discard_data[i].append(minlist.data[i][0])
                        # print("小",self.data[i], minlist.data[i][0])

                    if grubbs2.resultlist()[i][0] > G_t:
                        self.data[i].remove(maxlist.data[i][0])

                        discard_data[i].append(maxlist.data[i][0])
                        # print("大",self.data[i], maxlist.data[i][0])
            # print("bug",discard_data)
            # print("结果r",self.aclist)

        # Q法
        elif discard_method == "Q":
            # 计算Q计算
            minlist = roundac.first_min(self.aclist)[0]
            maxlist = roundac.first_max(self.aclist)[0]
            acrang =roundac.subtract(maxlist, minlist)

            q1 = roundac.divide(roundac.subtract(roundac.second_min(self.aclist)[0], minlist), acrang)
            q2 = roundac.divide(roundac.subtract(maxlist, roundac.second_max(self.aclist)[0]), acrang)

            # 获取Q表
            if confidence_discard is None:
                self.confidence_discard = 0.90
                row = 1  # 0.90
            if confidence_discard == 0.90:
                row = 1  # 0.90
            elif confidence_discard == 0.95:
                row = 2  # 0.95
            elif confidence_discard == 0.99:
                row = 3  # 0.95
            else:
                row = 1

            if shape[0] == 1:
                rank = int(number.data[0])
                q_t = Q_table[rank - 3][row]
                # print("初始",self.aclist)
                if q1.resultlist()[0] > q_t:
                    self.data.remove(minlist.data[0])
                    discard_data.append(minlist.data[0])
                if q2.resultlist()[0] > q_t:
                    self.data.remove(maxlist.data[0])
                    discard_data.append(maxlist.data[0])
            else:
                for i in range(shape[0]):
                    discard_data.append([])
                    rank = int(number.data[i])
                    q_t = Q_table[rank - 3][row]
                    # print(i,grubbs1.resultlist()[i][0],grubbs2.resultlist()[i][0],G_t)
                    if q1.resultlist()[i][0] > q_t:
                        self.data[i].remove(minlist.data[i][0])
                        discard_data[i].append(minlist.data[i][0])
                        # print("小",self.data[i], minlist.data[i][0])
                    if q2.resultlist()[i][0] > q_t:
                        self.data[i].remove(maxlist.data[i][0])
                        discard_data[i].append(maxlist.data[i][0])
                        # print("大",self.data[i], maxlist.data[i][0])

            # print("结果q", self.aclist)
        self.discard_data = discard_data
        self.aclist.updateshape()
        if renovate:
            self.statistics()

        return discard_data

    # 计算置信区间
    def confidence_interval_i(self, confidence_level_interval=None):
        # 获取t表
        resultlist = []
        if confidence_level_interval is None:
            self.confidence_level_interval = 0.95
            row = 2  # 0.95
        elif confidence_level_interval == 0.90:
            row = 1
        elif confidence_level_interval == 0.95:
            row = 2
        elif confidence_level_interval == 0.99:
            row = 3
        else:
            row = 2
        # !!!!

        if self.shape[0] == 1:
            rank = int(self.number.data[0])
            t_t = t_table[rank - 2][row]
            act_t = roundac.AnaChemList([t_t])
        else:
            act_t = []
            for i in range(self.shape[0]):
                act_t.append([])
                rank = int(self.number.data[i])
                t_t = t_table[rank - 2][row]
                act_t[i].append(t_t)
            act_t = roundac.AnaChemList(act_t)

            # 计算置信区间
        uncertainty = roundac.divide(roundac.multiply(act_t, self.sample_standard_deviation), roundac.power(self.number, roundac.AnaChemList(["0.5"]), 2))
        resultlist.append((self.mean, uncertainty))
        # else:
        #     for i in range(self.shape[0]):
        #         rank = int(self.number.data[i])
        #         t_t = t_table[rank - 2][row]

        return resultlist

    def describe(self):

        if self.shape[0] == 1:
            print("=" * 100)
            print("原始数据:")
            for i in self.aclist_copy.outputlist():
                print(i, end="\t")
            print()

            if self.discard_suspicious is True:
                print("处理离群值:使用{}法,置信度取{}%".format(self.discard_method, self.confidence_discard * 100), end="")
                if len(self.discard_data) > 0:
                    print("\n舍去的数据:", end="")
                    for i in self.discard_data:
                        print(i, end="\t")
                    print()
                else:
                    print(",没有数据被舍弃")

            print("置信度{}%对应置信区间:{}±{}"
                  .format(self.confidence_level_interval * 100, self.confidence_interval[0][0].data[0],
                          self.confidence_interval[0][1].data[0]))

            print("-" * 100)
            l1 = ["平均值       ",
                  "平均偏差     ",
                  "相对平均偏差  ",
                  "样本标准偏差  ",
                  "相对标准偏差  ",
                  "变异系数      ",
                  "复现性       "]
            l2 = [self.mean.outputlist()[0],
                  self.average_deviation.outputlist()[0],
                  self.relative_average_deviation.outputlist()[0],
                  self.sample_standard_deviation.outputlist()[0],
                  self.relative_standard_deviation.outputlist()[0],
                  self.coefficient_of_variation.outputlist()[0],
                  self.repeatability.outputlist()[0]]
            counter = 0
            for a1, a2 in zip(l1, l2):
                if counter == 2 or counter == 5:
                    print("{} {:<}% ".format(a1, a2))
                else:
                    print("{} {:<} ".format(a1, a2))
                counter += 1

            print("-" * 100)

            if self.true_value is None:
                print("{:10} {:10} {:10}".format("数据", "偏差", "相对偏差"))
                for i, j, k in zip(self.aclist.outputlist(), self.deviation.outputlist(), self.relative_deviation.outputlist()):
                    print("{:10} {:10} {:10}%".format(i, j, k))

            else:
                print("{:10} {:10} {:10} {:10} {:10}".format("数据", "误差", "相对误差", "偏差", "相对偏差"))
                for a1, a2, a3, a4, a5 in zip(self.aclist.outputlist(), self.error.outputlist(), self.relative_error.outputlist(), self.deviation.outputlist(), self.relative_deviation.outputlist()):
                    print("{:10} {:10} {:10}% {:10} {:10}%".format(a1, a2, a3, a4, a5))
            print("=" * 100, "\n", "\n")

        else:
            for group in range(self.shape[0]):
                print("=" * 100)
                print(f"第{group+1}组原始数据:")
                for i in self.aclist_copy.outputlist()[group]:
                    print(i, end="\t")
                print()

                if self.discard_suspicious is True:
                    print("处理离群值:使用{}法,置信度取{}%".format(self.discard_method, self.confidence_discard * 100),
                          end="")
                    # print(self.discard_data)
                    if len(self.discard_data[group]) > 0:
                        print("\n舍去的数据:", end="")
                        for i in self.discard_data[group]:
                            print(i, end="\t")
                        print()
                    else:
                        print(",没有数据被舍弃")
                #
                print("置信度{}%对应置信区间:{}±{}"
                      .format(self.confidence_level_interval * 100, self.confidence_interval[0][0].data[group][0],
                              self.confidence_interval[0][1].data[group][0]))
                # print("bug",self.confidence_interval,self.confidence_interval)

                print("-" * 100)
                l1 = ["平均值       ",
                      "平均偏差     ",
                      "相对平均偏差  ",
                      "样本标准偏差  ",
                      "相对标准偏差  ",
                      "变异系数     ",
                      "复现性       "]
                # print("bug",self.mean.outputlist())
                l2 = [self.mean.outputlist()[group][0],
                      self.average_deviation.outputlist()[group][0],
                      self.relative_average_deviation.outputlist()[group][0],
                      self.sample_standard_deviation.outputlist()[group][0],
                      self.relative_standard_deviation.outputlist()[group][0],
                      self.coefficient_of_variation.outputlist()[group][0],
                      self.repeatability.outputlist()[group][0]]
                counter = 0
                for a1, a2 in zip(l1, l2):
                    if counter == 2 or counter == 5:
                        print("{} {:<}% ".format(a1, a2))
                    else:
                        print("{} {:<} ".format(a1, a2))
                    counter += 1

                print("-" * 100)

                if self.true_value is None:
                    print("{:10} {:10} {:10}".format("数据", "偏差", "相对偏差"))
                    for i, j, k in zip(self.aclist.outputlist()[group], self.deviation.outputlist()[group], self.relative_deviation.outputlist()[group]):
                        print("{:10} {:10} {:10}".format(i, j, k))
                else:
                    print("{:10} {:10} {:10} {:10} {:10}".format("数据", "误差", "相对误差", "偏差", "相对偏差"))
                    for a1, a2, a3, a4, a5 in zip(self.aclist.outputlist()[group], self.error.outputlist()[group], self.relative_error.outputlist()[group],
                                                  self.deviation.outputlist()[group], self.relative_deviation.outputlist()[group]):
                        print("{:10} {:10} {:10} {:10} {:10}".format(a1, a2, a3, a4, a5))
                print("=" * 100, "\n", "\n")


if __name__ == "__main__":
    # a1 = roundac.AnaChemList([['0.3862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863'],
    #                           ['0.2862', '7859', '0.2851', '0.2848', '0.2852']])
    #     # [['0.2862', '7859', '0.2851', '0.2848', '0.2852'],
    # a2 =AnaChem(a1)
    # a2.discard()

    # a1 = roundac.AnaChemList([['0.2862', '7859', '0.2851', '0.2848', '0.2852'],
    #                          ['0.3862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863'],
    #                           ['0.2862', '7859', '0.2851', '0.2848', '0.2852']])
    #
    # a2 = AnaChem(a1)
    # a2.discard()
    # a1 = roundac.AnaChemList([['0.2862', '7859', '0.2851', '0.2848', '0.2852'],
    #                           ['0.3862', '0.2859', '0.2851', '0.2848', '0.2852', '0.2863'],
    #                           ['0.2862', '0.2851', '0.2848', '0.2852']])
    #
    # a2 = AnaChem(a1)
    # a2.discard(discard_method="Q")
    # # print(a2.confidence_interval)
    c1 = roundac.AnaChemList(['12', '12.1', '13.2', '11', '100'])
    c2 = AnaChem(c1, discard_suspicious=True, true_value=roundac.AnaChemList(['12.1']))
    c2.describe()
    c1 = roundac.AnaChemList([['12', '12.1', '13.2', '11','100'],['-23', '12', '12.1', '13.2', '11', '33']])
    c2 = AnaChem(c1, discard_suspicious=True, true_value=roundac.AnaChemList(['12.1','12.1']))
    c2.describe()
    # print(AnaChem)
    # help(AnaChem)
    # print(c2.discard_data,c2.data,c2.aclist)