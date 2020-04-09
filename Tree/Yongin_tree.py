import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc, style

df = pd.read_excel('경기도_용인시_가로수_20160501.xlsx', encoding='ISO-8859-1') # encoding='ISO-8859-1'은 'utf-8' codec can't decode byte 0xc1 in position 0: invalid start byte에 대한 해결방법
# 그래도 한글이 뜨지 않아 확인해보니 공공데이터의 경우 cp949로 인코딩 되는 경우가 많아서 그렇다고 함. 출처: https://teddylee777.github.io/python/%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%95%9C%EA%B8%80%EA%B9%A8%EC%A7%90%ED%98%84%EC%83%81-%ED%95%B4%EA%B2%B0%EB%B0%A9%EB%B2%95
# 그래도 안되길래 기존의 csv파일로 excel파일로 바꿔서 읽어들이니 잘 읽어옴.

#1.용인시 가로수의 수종과 각 수종별 심어진 횟수 조사. 참고:https://rfriend.tistory.com/tag/%EC%9C%A0%EC%9D%BC%ED%95%9C%20%EA%B0%92%EB%B3%84%EB%A1%9C%20%EA%B0%9C%EC%88%98%20%EC%84%B8%EA%B8%B0%20pd.Series.value_counts%28%29
sort_of_trees = []
sort_of_trees.extend(df['수목명'].unique())
numb_of_trees = []
numb_of_trees.extend(df['수목명'].value_counts())

semi_num_of_trees = df['수목명'].value_counts()

new_list = []
# 행의 index를 숫자로 조작할땐 iloc, 이름으로 조작할땐 loc


"""
https://nittaku.tistory.com/110
print(type(semi_num_of_trees)) -> <class 'pandas.core.series.Series'>
print(type(df)) -> <class 'pandas.core.frame.DataFrame'>
둘이 다른 타입이여서 데이터프레임 방식의 행 조작이 series에서 안먹혔었음. -> pd.DataFrame()으로 series를 묶어주면 dataframe으로 관리할 수 있음.
"""
for i in sort_of_trees:
    new_list.append([i, semi_num_of_trees["%s" %i]])

print(new_list[0][0])



plt.rcParams['figure.figsize'] = [12, 8]

group_names = []

for i in range(len(new_list)):
    group_names.append(new_list[i][0])

group_sizes = []

for i in range(len(new_list)):
    group_sizes.append(new_list[i][1])




group_explodes = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) # explode 1st slice

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')

plt.pie(group_sizes, 

        explode=group_explodes, 

        labels=group_names,  

        autopct='%1.2f%%', # second decimal place

        shadow=True, 

        startangle=90,

        textprops={'fontsize': 14}) # text font size

plt.axis('equal') #  equal length of X and Y axis

plt.title('Pie Chart of Market Share', fontsize=20)

plt.show()

# 4/9일자로 용인시 가로수 데이터 읽어서 (품종, 수량)을 pie chart로 표시하는 것 까지만 함. 다른 도시도 시도해볼 필요가 있으며, 차트 좀 예쁘게 꾸며야함.
# 수량 자체가 정확한 수치는 아니고 구획된 공간에 심어진 품종을 말해서 절대적인 수량은 맞지 않으나 어느 품종이 많이 심어졌는지에 대한 경향성 정도는 파악할 수 있음.




