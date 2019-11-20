import sqlite3
import pandas as pd
conn = sqlite3.connect('fin_deal.db')
c = conn.cursor()
df = pd.read_sql('SELECT * FROM deal', con = conn)
df.to_excel('fin_deal.xlsx', sheet_name = 'sheet1')

conn.close()


