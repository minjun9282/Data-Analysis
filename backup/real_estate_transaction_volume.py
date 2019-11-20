import sqlite3
import pandas as pd
#지역명과 전용면적을 입력할 경우 평균 값을 해당지역 매매가의 평균을 계산합니다.

def transaction_volume(data, size):
    
    
    conn = sqlite3.connect(data)

    min = size -1
    max = size +1

    df = pd.read_sql("SELECT * FROM new_deal WHERE %d<size AND size<%d" %(min, max), conn)

    transaction_volume = df.groupby(["ji_code","year", "month"])["day"].count()
    transaction_volume

    conn.close()
    return transaction_volume.to_excel('transaction_volume_59_20190304.xls')



