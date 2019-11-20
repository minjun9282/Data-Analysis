import sqlite3
import pandas as pd
from pandas import Series, DataFrame


con = sqlite3.connect('real_rent20180304.db')

conn1 = sqlite3.connect('real_trade2018_03.db')
conn2 = sqlite3.connect('real_trade2018_04.db')



df1 = pd.read_sql("SELECT * FROM lent", conn1, index_col=None)
df2 = pd.read_sql("SELECT * FROM lent", conn2, index_col=None)


#11/10 attach database문 실패함, pandas도입하여 dataframe으로 변환하여 database합치는거 시도함. 특정 column만 읽어내는 것을 통해 아파트 목록 - 학구도를 연결하고자함. 학구도 관련 api를 찾아보고 관련 방법을 모색했음. 추가적으로 connection을 close해야하는데 cursor를 close하는 실수 저지름.
new_db1 = pd.concat([df1,df2]) #df1, df2를 [df1, df2]로 싸줘야함..


new_db1.to_sql('rent', con)


con.close()
conn1.close()
conn2.close()


#rent는 따로 rent.py에다가 써야하는데 그냥 deals.py위에 덮어써버렸다.

