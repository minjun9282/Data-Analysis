import pandas as pd
import sqlite3

conn = sqlite3.connect('g_m_ent_rate.db')

df = pd.read_excel('gm.xls')