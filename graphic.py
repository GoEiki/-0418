import copy
import csv
import matplotlib as mpl
#mpl.use('TkAgg')
import matplotlib.pyplot as plt
#plt.rcParams['font.family'] = "AppleGothic"
import numpy as np

# Data2クラス
# コンストラクタ() -> None
#  引数：csv_data_name:str = "A1_1.csv"
#   データが格納されているcsvファイルを開きます。データは2次元を想定しています。
# x -> list
#  コンストラクタの引数csv_data_nameをもとに開いたデータ内の入力に値するところを返します。
#  格納順はyと対応しています。
#  配列内は全てfloatです。
#  配列はn✖️2で返します。
# y -> list
#  コンストラクタの引数csv_data_nameをもとに開いたデータ内の正解クラスに値するところを返します。
#  格納順はxと対応しています。
#  配列内は全てintです。
#  配列はn✖️1で返します。
# data -> list
#  コンストラクタの引数csv_data_nameをもとに開いたデータを返します。
#  それぞれのデータごとにタプルで格納しています。例:([0.2, 0.5], 0)
#  配列は要素数nで返します。
class Data2(object):
  def __init__(self, csv_data_name:str = "A1_1.csv") -> None:
    self.__data_set = []
    self.__data_x = []
    self.__data_y = []
    with open(csv_data_name, "r") as f:
      reader = csv.reader(f)
      for i, row in enumerate(reader):
        if i > 1:
          self.__data_x.append([float(row[0]), float(row[1])])
          self.__data_y.append(int(row[2]))
          self.__data_set.append((self.__data_x[-1], self.__data_y[-1]))
  
  @property
  def x(self) -> list:
    return copy.deepcopy(self.__data_x)

  @property
  def y(self) -> list:
    return copy.deepcopy(self.__data_y)

  @property
  def data(self) -> list:
    return copy.deepcopy(self.__data_set)

# Graphic2クラス
# コンストラクタ() -> None
#  引数：なし
# print_graph() -> None
#  データと現在の二値分類の境界を視覚的に表示します
#  ただし，グラフを閉じないと次のコードを実行できないので注意
#  引数：data:Data2.data
#   Data2クラスのdataを格納してください
#  引数；w:list
#   重みを配列で格納してください。
#   注意：配列内は以下のようにしてください
#    w = [w0, w1, w2]
#    ただし，w0はバイアス項
class Graphic2(object):
  def __init__(self) -> None:
    pass

  def print_graph(self, data, w:list = None) -> None:
    if w is None:
      w = [0, 0, 1]
    line_x = np.linspace(0,1,num=100)
    line_y = -(w[1 ]/ w[2]) * line_x - (w[0] / w[2])
    plt.plot(line_x, line_y, color = "black")
    plt.xlabel("x1")
    plt.ylabel("x2")
    c0 = np.array([d[0] for d in data if d[1] == 0])
    c1 = np.array([d[0] for d in data if d[1] == 1])
    plt.scatter(c0[:, 0], c0[:, 1], color = "red", label = "0")
    plt.scatter(c1[:, 0], c1[:, 1], color = "green", label = "1")
    plt.legend()
    plt.text(0, -0.05, "w0=" + str(w[0]) + ", w1=" + str(w[1]) + ", w2=" + str(w[2]))
    plt.show()

if __name__ =='__main__':
  d = Data2()
  g = Graphic2()
  g.print_graph(d.data)