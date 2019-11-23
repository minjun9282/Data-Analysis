import sqlite3
import pandas as pd
from work_distance import work_loc_rec

def realestate_recommend(min_price, max_price, size, first_work_loc, second_work_loc):
    
    conn = sqlite3.connect('real_deal20190304.db')

    min_size = size -1
    max_size = size +1

    work_loc_name_list = list(work_loc_rec(first_work_loc, second_work_loc).keys())
    no_dup_list = ['41285 고양시 일산동구', '41190 부천시', '41287 고양시 일산서구', '41290 과천시', '41170 안양시', '11470 양천구', '11440 마포구', '41570 김포시', '11260 중랑구', '41465 용인시 수지구', '41800 연천군', '41650 포천시', '41133 성남시 중원구', '41390 시흥시', '11560 영등포구', '41150 의정부시', '41280 고양시', '11740 강동구', '41270 안산시', '41480 파주시', '11200 성동구', '11350 노원구', '11320 도봉구', '11500 강서구', '41130 성남시', '41610 광주시', '41430 의왕시', '41630 양주시', '11650 서초구', '41450 하남시', '41117 수원시 영통구', '11215 광진구', '41113 수원시 권선구', '41220 평택시', '11230 동대문구', '41550 안성시', '11380 은평구', '11545 금천구', '41500 이천시', '41273 안 산시 단원구', '41271 안산시 상록구', '41210 광명시', '11140 중구', '41110 수원시', '41460 용인시', '41590 화성시', '11710 송파구', '41410 군포시', '41135 성남시 분당구', '41281 고양시 덕양구', '41173 안양시 동안구', '41360 남양주시', '41670 여주시', '11620 관악구', '11680 강남구', '41461 용인시 처인구', '11590 동작구', '41171 안양시 만안구', '41115 수원시 팔달구', '41250 동두천시', '41830 양평군', '11530 구로구', '11410 서대문구', '41820 가평군', '11290 성북구', '11305 강북구', '41131 성남시 수정구', '41463 용인시 기흥구', '41111 수원시 장안구', '41310 구리시', '41370 오산시', '11110 종로구', '11170 용산구']
    
    work_loc_code_list = []

    for i in range(len(work_loc_name_list)):
        for j in range(len(no_dup_list)):
            if work_loc_name_list[i] == no_dup_list[j].split()[-1]:
                work_loc_code_list.append(int(no_dup_list[j].split()[0]))
    

    data = {'build_y':[1999],'apt_nm':['오민준'],'gu_price':[531], 'size':[200] ,'ji_code':[100], 'dong':['오민준'], '지역명':['오씨가문']}

    final_df = pd.DataFrame(data, columns=['build_y','apt_nm','gu_price', 'size' ,'ji_code', 'dong'])

    for i in range(len(work_loc_name_list)):
        globals()['df{}'.format(i)] = pd.read_sql("SELECT build_y, apt_nm, gu_price, size, ji_code, dong FROM deal WHERE %d<size AND size<%d AND gu_price<%d AND %d<gu_price AND ji_code == %s" %(min_size, max_size, max_price, min_price, work_loc_code_list[i]), conn)
        globals()['df{}'.format(i)]['지역명'] = work_loc_name_list[i]
        final_df = pd.concat([final_df, globals()['df{}'.format(i)]])

    return final_df.to_excel('ss.xls', sheet_name='Sheet1')

realestate_recommend(100000, 111000, 84, '강남구', '마포구')