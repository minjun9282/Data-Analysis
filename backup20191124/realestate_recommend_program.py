def main():
    from realestate_recommend import realestate_recommend
    print('현재 반영된 최신 실거래가 자료는 2020년 1월자 자료입니다.(수정일 2020년 2월 23일)')
    print('이 프로그램은 부동산 매매 추천 프로그램입니다.')
    print('현재 프로그램은 서울시와 경기도의 지역만 검색이 가능합니다.')
    print('예산의 최소금액 및 최대금액, 구하고자 하는 아파트의 전용면적, 본인과 배우자의 직장위치를 입력하시면 됩니다.')
    print('추천되는 지역은 학군과 직주근접 요소가 고려된 지역입니다. 본인의 조건과 맞는 해당 지역의 아파트 명과 함께 최근 4개월 실거래가 중위값을 알려드립니다.')
    print('엑셀에 표시되는 dong은 행정동, apt_nm은 아파트 이름, build_y는 건축연도, gu_price는 실거래가 중위값(단위: 만원)을 의미합니다.')
    print('조건에 맞는 데이터가 없을 경우 오류가 발생할 수 있습니다.')
    min_price = int(input("예산의 최소 금액을 입력하세요: (단위:만원)"))
    max_price = int(input("예산의 최대 금액을 입력하세요: (단위:만원)"))
    size = int(input("찾고 계신 아파트의 전용면적을 입력하세요: (단위:m^2)"))
    print('지역명은 구/군 단위로 구/군이 없을 경우 시 단위로 입력해주세요. (ex) 강남구, 수지구, 시흥시)')
    first_work_loc = input('본인이나 배우자의 직장 위치 중 우선시 되는 지역을 입력하세요: ')
    print('두 지역이 동일하거나 본인이 미혼인 경우 앞의 값과 동일 한 값을 입력하세요.')
    second_work_loc = input('본인이나 배우자의 직장 위치 중 차선시 되는 지역을 입력하세요: ')
    print('이제 추천 리스트의 작성이 끝났습니다. 추천 리스트는 원하시는 파일명의 엑셀 파일로 저장됩니다. ')
    filename = input('파일명을 입력하세요: ')
    print('개발자: 소프트웨어융합학과 오민준')
    realestate_recommend(min_price, max_price, size, first_work_loc, second_work_loc, filename)
    
if __name__=="__main__":
    main()
