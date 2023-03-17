
def question1(num):     # 各位数字之和
    sum = 0
    for i in range(len(str(num))):
        sum += num%10
        num //= 10
    print(sum, '\n')


def question2():    # 交集、并集、和差集
    setA = {1, 2, 'str', 'abc'}
    setB = {2, 'abc', 9}
    print('交集:', setA.intersection(setB))
    print('并集:', setA.union(setB))
    print('差集:', setA.difference(setB), '\n')


def question3():    # 二进制、八进制、十六进制
    num = 128
    print('二进制:', bin(num))
    print('八进制:', oct(num))
    print('十六进制:', hex(num), '\n')


def question4():    # 偶数列表
    list = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345]
    list2 = []
    for num in list:
        if num%2==0:
            list2.append(num)
    print(list2, '\n')


def question5():    # 降序排列
    list = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345]
    list.sort(reverse=True)
    print(list, '\n')


def question6():    # 连乘
    sum = 1
    list = [1, 2, 3, 4, 5]
    for num in list:
        sum *=num
    print(sum, '\n')


def question7():    # 统计次数
    str = 'hello world'
    dic = {}
    for i in str:
        if i not in dic:
            dic[i] = 1  # 不在字典中就加入
        else:
            dic[i]+=1   #
    num = max(dic.values())    # 出现最多的次数
    for i,j in dic.items():
        if j == num:
            print(f'出现最多的字符是:{i}出现了{j}次')


if __name__=='__main__':
    question1(3459)
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
