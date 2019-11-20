import sqlite3
import pandas as pd
from pandas import DataFrame

conn1 = sqlite3.connect('fin_deal.db')
conn2 = sqlite3.connect('fin_rent.db')
c1 = conn1.cursor()
c2 = conn2.cursor()

df1 = pd.read_sql("SELECT * FROM DEAL", conn1, index_col=None)
df2 = pd.read_sql("SELECT * FROM RENT", conn2, index_col=None)

"""
new_set1 = {}
new_list1 = []
for a in df1.apt_nm:
    new_list1.append(a)
new_set1 = set(new_list1)

new_set2 = {}
new_list2 = []
for a in df2.apt_nm:
    new_list2.append(a)
new_set2 = set(new_list2)




print(len(new_set1)) #11761
print(len(new_set2)) #13472

apt_nm = new_set1|new_set2

print(len(apt_nm)) #201701~201910 까지의 전월세/매매 거래된 단지 수는 총 13472개
"""

conn1.close()
conn2.close()

df1["dong_apt_nm"] = df1['dong'] + ' ' + df1['apt_nm']
df2["dong_apt_nm"] = df2['dong'] + ' ' + df2['apt_nm']

new_set1 = {}
new_list1 = []
for a in df1.dong_apt_nm:
    new_list1.append(a)
new_set1 = set(new_list1)

new_set2 = {}
new_list2 = []
for a in df2.dong_apt_nm:
    new_list2.append(a)
new_set2 = set(new_list2)

SD_dong_apt_nm = list(new_set1|new_set2)
print(SD_dong_apt_nm[0:4])


