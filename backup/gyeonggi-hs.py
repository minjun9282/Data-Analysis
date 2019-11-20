import sqlite3
import pandas as pd
import numpy as np
#지역명과 전용면적을 입력할 경우 평균 값을 해당지역 매매가의 평균을 계산합니다.

def highschool(data):

    df = pd.read_excel(data, sheet_name='졸업생의 진로 현황(고과정 고등학교)')

    new_df = df.groupby(["기준년도","지역명"]).sum()
    

    return new_df.to_excel('gyeonggi_ent_rate.xlsx')
    



highschool('gh.xls')