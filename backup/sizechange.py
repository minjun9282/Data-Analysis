import sqlite3
import pandas as pd
#size column의 모든 값을 실수형태로 바꿔주기 위한 py입니다.
conn = sqlite3.connect('real_rent20190304.db')
df = pd.read_sql("SELECT * FROM lent", conn, index_col=None)
df['size'] = pd.to_numeric(df['size'])
df.to_sql('new_rent', conn)