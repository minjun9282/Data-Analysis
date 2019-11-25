import sqlite3
import pandas as pd
from work_distance import work_loc_rec
from operator import itemgetter
import numpy as np

def realestate_recommend(min_price, max_price, size, first_work_loc, second_work_loc, filename):
    
    conn = sqlite3.connect('real_deal20190304.db')

    min_size = size -1
    max_size = size +1

    work_loc_name_list = list(work_loc_rec(first_work_loc, second_work_loc).keys())
    no_dup_list = ['41285 고양시 일산동구', '41190 부천시', '41287 고양시 일산서구', '41290 과천시', '41170 안양시', '11470 양천구', '11440 마포구', '41570 김포시', '11260 중랑구', '41465 용인시 수지구', '41800 연천군', '41650 포천시', '41133 성남시 중원구', '41390 시흥시', '11560 영등포구', '41150 의정부시', '41280 고양시', '11740 강동구', '41270 안산시', '41480 파주시', '11200 성동구', '11350 노원구', '11320 도봉구', '11500 강서구', '41130 성남시', '41610 광주시', '41430 의왕시', '41630 양주시', '11650 서초구', '41450 하남시', '41117 수원시 영통구', '11215 광진구', '41113 수원시 권선구', '41220 평택시', '11230 동대문구', '41550 안성시', '11380 은평구', '11545 금천구', '41500 이천시', '41273 안 산시 단원구', '41271 안산시 상록구', '41210 광명시', '11140 중구', '41110 수원시', '41460 용인시', '41590 화성시', '11710 송파구', '41410 군포시', '41135 성남시 분당구', '41281 고양시 덕양구', '41173 안양시 동안구', '41360 남양주시', '41670 여주시', '11620 관악구', '11680 강남구', '41461 용인시 처인구', '11590 동작구', '41171 안양시 만안구', '41115 수원시 팔달구', '41250 동두천시', '41830 양평군', '11530 구로구', '11410 서대문구', '41820 가평군', '11290 성북구', '11305 강북구', '41131 성남시 수정구', '41463 용인시 기흥구', '41111 수원시 장안구', '41310 구리시', '41370 오산시', '11110 종로구', '11170 용산구']
    
    #work_loc_name_list를 좀 줄여주기 by 학군 및 상승률 및 직주근접요소
    if size == 84:
        ratings = pd.read_csv('real_deal_84.csv')
    elif size == 59:
        ratings = pd.read_csv('real_deal_59.csv')
    else:
        ratings = pd.read_csv('real_deal_84.csv')

    work_loc_code_list = []

    for i in range(len(work_loc_name_list)):
        for j in range(len(no_dup_list)):
            if work_loc_name_list[i] == no_dup_list[j].split()[-1]:
                work_loc_code_list.append(int(no_dup_list[j].split()[0]))


    data = {'build_y':[1999],'apt_nm':['오민준'],'gu_price':[531], 'size':[200] ,'ji_code':[100], 'dong':['오민준'], '지역명':['오씨가문']} #데이터프레임 결합을 위해 임의로 한 줄 넣었습니다..

    final_df = pd.DataFrame(data, columns=['build_y','apt_nm','gu_price', 'size' ,'ji_code', 'dong'])

    new_work_loc_name_list = []

    for i in range(len(work_loc_name_list)):
        globals()['df{}'.format(i)] = pd.read_sql("SELECT build_y, apt_nm, gu_price, size, ji_code, dong FROM deal WHERE %d<size AND size<%d AND gu_price<%d AND %d<gu_price AND ji_code == %s" %(min_size, max_size, max_price, min_price, work_loc_code_list[i]), conn)
        globals()['df{}'.format(i)]['지역명'] = work_loc_name_list[i]
        new_work_loc_name_list.append(work_loc_name_list[i])
        middle_df = pd.concat([final_df, globals()['df{}'.format(i)]])

    middle_df = middle_df.drop(0,0)

    
    ratings = ratings[['지역명', 'recommend ratings']]
    
    local_name_with_ratings = []

    for i in new_work_loc_name_list:
        for j in range(len(ratings)):
            if i == ratings.loc[j, '지역명']:
                local_name_with_ratings.append((i, ratings.loc[j, 'recommend ratings'])) 

    
    
    local_name_with_ratings.sort(key=itemgetter(1), reverse=True)

    if len(new_work_loc_name_list) > 8:
        del local_name_with_ratings[8:]
    
    work_loc_code_list = []

    for i in range(len(local_name_with_ratings)):
        for j in range(len(no_dup_list)):
            if local_name_with_ratings[i][0] == no_dup_list[j].split()[-1]:
                work_loc_code_list.append(int(no_dup_list[j].split()[0]))
    
    for i in range(len(local_name_with_ratings)):
        globals()['df{}'.format(i)] = pd.read_sql("SELECT build_y, apt_nm, gu_price, size, ji_code, dong FROM deal WHERE %d<size AND size<%d AND gu_price<%d AND %d<gu_price AND ji_code == %s" %(min_size, max_size, max_price, min_price, work_loc_code_list[i]), conn)
        globals()['df{}'.format(i)]['지역명'] = local_name_with_ratings[i][0]
        final_df = pd.concat([final_df, globals()['df{}'.format(i)]])

    final_df = final_df.drop(0,0)

    #final df에서 이제 중복되는 아파트 단지명은 하나로 합치되 최소 실거래가와 최대 실거래가만 보여주기.
    final_df['gu_price'] = final_df['gu_price'].values.astype(np.int64)

    recommend_df = final_df.groupby(["지역명",'dong',"apt_nm","build_y"])["gu_price"].median()
    
    conn.close()

    
    return recommend_df.to_excel('%s.xls'%filename, sheet_name = 'Sheet1')
