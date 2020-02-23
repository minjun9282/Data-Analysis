import pandas as pd
import sqlite3

def excel_to_db(filename, db_name, tablename):
    conn = sqlite3.connect('%s' %db_name)
    df = pd.read_excel('%s' %filename)
    df.to_sql('%s' %tablename, conn)

excel_to_db('real_deal202001.xls', 'new_real_deal202021.db', 'deal')