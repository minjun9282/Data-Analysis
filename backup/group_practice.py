import pandas as pd
import sqlite3

conn = sqlite3.connect('real_rent20170102.db')
df = pd.read_sql("SELECT * FROM rent", conn, index_col=None)

print(df["bo_price"].groupby(df['ji_code']))