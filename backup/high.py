import pandas as pd
import sqlite3

conn = sqlite3.connect('g_h_ent_rate.db')

df = pd.read_excel('gm.xls')

def middle(year, local, excel_data):
    df = excel_data
    new_df = df.loc[(df['기준년도'] == year) & (df['지역명'] == local) , ['기준년도','지역명','졸업합계(명)','일반고진학합계(명)','특성화고진학합계(명)','(특수목적고)과학고진학합계(명)','(특수목적고)외고ㆍ국제고진학합계(명)','(특수목적고)예고ㆍ체고진학합계(명)','(특수목적고)마이스터고진학합계(명)','(자율고)자율형사립고진학합계(명)','(자율고)자율형공립고진학합계(명)'] ]
    new_df.loc["total"] = new_df.sum(axis=0)
    new_df['기준년도'] = year
    new_df['지역명'] = local
    return new_df.loc[["total"],:]

new_set = {}
new_list = []
for a in df['지역명']:
    new_list.append(a)
g_local = list(set(new_list))

g_local = ['경기도 평택시', '경기도 안산시 단원구', '경기도 시흥시', '경기도 수원시 영통구', '경기도 하남시', '경기도 수원시 권선구', '경기도 안양시 만안구', '경기도 오산시', '경기도 안성시', '경기도 의정부시', '경기도 고양시 일산서구', '경기도 연천군', '경기도 화성시', '경기도 여주시', '경기도 광주시', '경기도 성남시 중원구', '경기도 구리시', '경기도 양주시', '경기도 광명시', '경기도 부천시', '경기도 고양시 일산동구', '경기도 김포시', '경기도 고양시 덕양구', '경기도 양평군', '경기도 파주시', '경기도 수원시 장안구', '경기도 용인시 기흥구', '경기도 의왕시', '경기도 남양주시', '경기도 동두천시', '경기도 가평군', '경기도 성남시 수정구', '경기도 안산시 상록구', '경기도 이천시', '경기도 포천시', '경기도 용인시 처인구', '경기도 과천시', '경기도 안양시 동안구', '경기도 수원시 팔달구', '경기도 성남시 분당구', '경기도 군포시', '경기도 용인시 수지구']
inv_year = [2017, 2018]

def middle_total(year, local, data, sql3):
    g_m_ent_rate = pd.DataFrame()
    for i in year:
        for j in local:
            df1 = middle(i, j, data)
            g_m_ent_rate = g_m_ent_rate.append(df1)
    
    return g_m_ent_rate.to_sql('g_m_ent_rate', sql3)

middle_total(inv_year, g_local, df, conn)

conn.close()