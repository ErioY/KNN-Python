'''
@Autor: ErioY
@Date: 2019-10-05 13:34:26
@Email: 1973545559@qq.com
@Github: https://github.com/ErioY
@LastEditors: ErioY
@LastEditTime: 2019-10-06 21:38:10
'''
import math
# 训练集
train_data = {"亲密旅行": [45, 2, 9, "喜剧片"],
              "新喜剧之王": [21, 17, 5, "喜剧片"],
              "唐人街探案2": [54, 9, 11, "喜剧片"],
              "羞羞的铁拳": [39, 0, 31, "喜剧片"],
              "复仇者联盟4": [5, 2, 57, "动作片"],
              "蜘蛛侠：英雄远征": [3, 2, 65, "动作片"],
              "速度与激情8": [2, 3, 55, "动作片"],
              "战狼2": [6, 4, 21, "动作片"],
              "无问西东": [7, 46, 4, "爱情片"],
              "后来的我们": [9, 39, 8, "爱情片"],
              "悲伤逆流成河": [9, 38, 2, "爱情片"],
              "超时空同居": [8, 34, 17, "爱情片"]}
# 测试集
test_data = [33, 4, 25]
KNN = []
# 遍历计算测试集与数据集中所有数据的距离
for key, value in train_data.items():
    # 求距离
    d = math.sqrt((test_data[0] - value[0]) ** 2 + (test_data[1] - value[1]) ** 2 + (test_data[2] - value[2]) ** 2)
    # 取小数点后两位
    KNN.append([key, round(d, 2)])
# 按距离大小升序并取前 5 项
KNN.sort(key=lambda dis: dis[1])
KNN = KNN[:  5]
# print(KNN)
# 类别
labels = {
    "喜剧片": 0,
    "动作片": 0,
    "爱情片": 0
}
# 确定前 5 个样本所在类别出现的频率
for i in KNN:
    # 取出训练集的列表
    label = train_data[i[0]]
    # 确定出现的次数
    labels[label[3]] += 1
# 对所得结果按照出现的次数倒序
labels = sorted(labels.items(), key=lambda l: l[1], reverse=True)
# 输出排序后的结果和出现频率最高的类别
print("前5个样本所在类别出现的次数为：", labels)
print("《美人鱼》属于", labels[0][0])
