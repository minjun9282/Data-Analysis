import pandas as pd
import sqlite3

def excel_to_db(filename, db_name, tablename):
    conn = sqlite3.connect('%s' %db_name)
    df = pd.read_excel('%s' %filename)
    df.to_sql('%s' %tablename, conn)

excel_to_db('real_deal202001.xls', 'new_real_deal202001.db', 'deal')
# 잠시 실거래가 db를 최신 자료로 업데이트 해주기 위해 사용한 간단한 코드임. 아파트 매매가격의 숫자 구분자 ','로 인한 오류는 일단 엑셀의 기능으로 수정함.
