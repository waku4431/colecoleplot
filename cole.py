import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from galvani import BioLogic as BL

mpr1=BL.MPRfile('2_01_PEIS_C01.mpr')
mpr2=BL.MPRfile('2_02_PEIS_C01.mpr')
mpr3=BL.MPRfile('2_03_PEIS_C01.mpr')
mpr4=BL.MPRfile('2_04_PEIS_C01.mpr')
mpr5=BL.MPRfile('2_05_PEIS_C01.mpr')
mpr6=BL.MPRfile('2_06_PEIS_C01.mpr')
mpr7=BL.MPRfile('2_07_PEIS_C01.mpr')
mpr8=BL.MPRfile('2_08_PEIS_C01.mpr')
mpr9=BL.MPRfile('2_09_PEIS_C01.mpr')
mpr10=BL.MPRfile('2_10_PEIS_C01.mpr')
mpr11=BL.MPRfile('2_11_PEIS_C01.mpr')

df1=pd.DataFrame(mpr1.data)
df2=pd.DataFrame(mpr2.data)
df3=pd.DataFrame(mpr3.data)
df4=pd.DataFrame(mpr4.data)
df5=pd.DataFrame(mpr5.data)
df6=pd.DataFrame(mpr6.data)
df7=pd.DataFrame(mpr7.data)
df8=pd.DataFrame(mpr8.data)
df9=pd.DataFrame(mpr9.data)
df10=pd.DataFrame(mpr10.data)
df11=pd.DataFrame(mpr11.data)


plt.scatter(df1["Re(Z)/Ohm"],df1["-Im(Z)/Ohm"],label="1.5V") #第一引数に横軸の配列，第二引数に縦軸の配列
plt.scatter(df2["Re(Z)/Ohm"],df2["-Im(Z)/Ohm"],label="1.6V") 
plt.scatter(df3["Re(Z)/Ohm"],df3["-Im(Z)/Ohm"],label="1.7V") 
plt.scatter(df4["Re(Z)/Ohm"],df4["-Im(Z)/Ohm"],label="1.8V") 
plt.scatter(df5["Re(Z)/Ohm"],df5["-Im(Z)/Ohm"],label="1.9V") 
plt.scatter(df6["Re(Z)/Ohm"],df6["-Im(Z)/Ohm"],label="2.0V") 
plt.scatter(df7["Re(Z)/Ohm"],df7["-Im(Z)/Ohm"],label="2.1V") 
plt.scatter(df8["Re(Z)/Ohm"],df8["-Im(Z)/Ohm"],label="2.2V") 
plt.scatter(df9["Re(Z)/Ohm"],df9["-Im(Z)/Ohm"],label="2.3V") 
plt.scatter(df10["Re(Z)/Ohm"],df10["-Im(Z)/Ohm"],label="2.4V") 
plt.scatter(df11["Re(Z)/Ohm"],df11["-Im(Z)/Ohm"],label="2.5V") 

plt.legend()
plt.legend(loc="lower right",borderaxespad=0,fontsize=20,markerscale=3,framealpha=0)

plt.xlabel('Re(Z)/Ohm',fontsize=30) #横軸ラベル名
plt.ylabel('-Im(Z)/Ohm',fontsize=30) #縦軸ラベル名
plt.tick_params(labelsize=30)#軸の目盛りのフォントサイズ

df11=df11.abs()#絶対値に変換
df11=df11.sort_values(by='-Im(Z)/Ohm')

print(df11.loc[150,'Re(Z)/Ohm'])

plt.text(0.250, 0.075, df11.loc[150,'Re(Z)/Ohm'], fontsize=50)

plt.xlim(0.1,0.3)#x軸の範囲
plt.ylim(-0.1,0.1)#y軸の範囲
plt.grid()

plt.show()