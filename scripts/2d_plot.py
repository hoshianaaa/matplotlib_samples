# matplotlibライブラリの呼び出し。今後pltの3文字で呼び出しができるように as plt としている。
import matplotlib.pyplot as plt
 
# データを用意
y = [1, 2, 1, 2,1]
x = range(0,len(y))
 
# 描画オブジェクト（fig）とサブプロット（ax）を生成する
fig, ax = plt.subplots()
 
# 折れ線グラフ表示
ax.plot(x, y)
# グラフにタイトルをつける
ax.set_title('テストタイトル',fontname='Meiryo')
# x軸の軸ラベルを設定
plt.xlabel('x')
# y軸の軸ラベルを設定
plt.ylabel('y')
 
# グラフを表示
plt.show()
