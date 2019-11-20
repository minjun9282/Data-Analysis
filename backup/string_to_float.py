import sqlite3
import pandas as pd
conn = sqlite3.connect('real_rent20190304.db')

df = pd.read_sql('SELECT * FROM lent', con = conn)
df.to_excel('real_rent20190304.xlsx', sheet_name = 'sheet1')

conn.close()