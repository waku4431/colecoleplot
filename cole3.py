import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from galvani import BioLogic as BL
import glob

gl = glob.glob('*.mpr')

for i in range(len(gl)):
    mpr=BL.MPRfile(gl[i])
    df=pd.DataFrame(mpr.data)
    plt.scatter(df["Re(Z)/Ohm"],df["-Im(Z)/Ohm"],label=f'{round(2.5-0.1*i,2)}V')

plt.legend()

plt.legend(loc="lower right",borderaxespad=0,fontsize=20,markerscale=3,framealpha=0)
plt.xlabel('Re(Z)/Ohm',fontsize=30) #横軸ラベル名
plt.ylabel('-Im(Z)/Ohm',fontsize=30) #縦軸ラベル名
plt.tick_params(labelsize=30)#軸の目盛りのフォントサイズ

plt.xlim(0.1,0.3)#x軸の範囲
plt.ylim(-0.1,0.1)#y軸の範囲
plt.grid()

plt.show()
