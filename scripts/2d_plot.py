# matplotlibライブラリの呼び出し。今後pltの3文字で呼び出しができるように as plt としている。
import matplotlib.pyplot as plt
 
# データを用意

y = [1, 255, 255, 255,255, 0]
x = list(range(0,len(y)))
print(x)
fig, ax = plt.subplots(nrows=6,ncols=1)

while True:
# 描画オブジェクト（fig）とサブプロット（ax）を生成する
   
# 折れ線グラフ表示
  ax[0].plot(x, y)
# グラフにタイトルをつける
  ax[0].set_title('sample',fontname='Meiryo')
# x軸の軸ラベルを設定
  plt.xlabel('x')
# y軸の軸ラベルを設定
  plt.ylabel('y')
   
# グラフを表示
#plt.show()
  plt.pause(0.1)
  ax[0].lines[0].remove()
  plt.cla()
  y[0] = y[0] + 0.1
  print(x,y)
