import sqlite3
import pandas as pd

def db_to_excel(db_name, tablename, filename):
    conn = sqlite3.connect('%s' %db_name)
    df = pd.read_sql("SELECT * FROM %s" %tablename, conn)
    df.to_excel('%s' %filename)
