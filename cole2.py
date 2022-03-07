import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from galvani import BioLogic as BL#.mprから配列を取得する
import glob#フォルダ内のファイル一覧を取得する

#直列セル抵抗の値を求める
mpr=BL.MPRfile('2_01_PEIS_C01.mpr')
df=pd.DataFrame(mpr.data)

df=df.abs()#絶対値に変換
df.sort_values=df["-Im(Z)/Ohm"]

print(df.loc[150,'Re(Z)/Ohm'])


