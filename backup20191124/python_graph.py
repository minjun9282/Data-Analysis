import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
'''
#1. 손익과 상승률 2차원 그래프 그리기

#1-1 전용면적 84
df = pd.read_csv('real_deal_84.csv')

sns.set(style = "darkgrid")

g1 = sns.relplot(x="top 25% return (%)", y="top 25% gain and loss (unit: 10000won)", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["top 25% return (%)"][name]*1.01, df["top 25% gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g2 = sns.relplot(x="top 25% return (%)", y="top 25% gain and loss (unit: 10000won)", data= df, hue ='local_name', size = '중학교 학군 점수')
for name in df.index:
    plt.text(df["top 25% return (%)"][name]*1.01, df["top 25% gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g3 = sns.relplot(x="top 25% return (%)", y="top 25% gain and loss (unit: 10000won)", data= df, hue ='local_name', size = '고등학교 학군 점수')
for name in df.index:
    plt.text(df["top 25% return (%)"][name]*1.01, df["top 25% gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g4 = sns.relplot(x="top 25% return (%)", y="top 25% gain and loss (unit: 10000won)", data= df, hue ='local_name', size = '중학교 + 고등학교 학군 점수')
for name in df.index:
    plt.text(df["top 25% return (%)"][name]*1.01, df["top 25% gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()



#1-2 전용 면적 59

sns.set(style = "darkgrid")

df = pd.read_csv('real_deal_59.csv')

g1 = sns.relplot(x="top 25% return (%)", y="top 25% gain and loss (unit: 10000won)", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["top 25% return (%)"][name]*1.01, df["top 25% gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g2 = sns.relplot(x="top 25% return (%)", y="top 25% gain and loss (unit: 10000won)", data= df, hue ='local_name', size = '중학교 학군 점수')
for name in df.index:
    plt.text(df["top 25% return (%)"][name]*1.01, df["top 25% gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g3 = sns.relplot(x="top 25% return (%)", y="top 25% gain and loss (unit: 10000won)", data= df, hue ='local_name', size = '고등학교 학군 점수')
for name in df.index:
    plt.text(df["top 25% return (%)"][name]*1.01, df["top 25% gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g4 = sns.relplot(x="top 25% return (%)", y="top 25% gain and loss (unit: 10000won)", data= df, hue ='local_name', size = '중학교 + 고등학교 학군 점수')
for name in df.index:
    plt.text(df["top 25% return (%)"][name]*1.01, df["top 25% gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()



#2. 평균가/중앙값과 학군 2차원 그래프 그리기. data, 중위값 or 평균값 , middle shcool rating or high school rating or middle + high school rating 선택시 원하는 그래프 얻을 수 있음.

#2-1 전용면적 84
sns.set(style = "darkgrid")

df = pd.read_csv('real_deal_84.csv')

gm = sns.relplot(x="average price (unit:10000won)", y="middle school rating", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["average price (unit:10000won)"][name]*1.01, df["middle school rating"][name], df['local_name'][name])

plt.show()

#2-2 전용면적 59

sns.set(style = "darkgrid")

df = pd.read_csv('real_deal_59.csv')

gh = sns.relplot(x="average price (unit:10000won)", y="middle school rating", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["average price (unit:10000won)"][name]*1.01, df["middle school rating"][name], df['local_name'][name])

plt.show()


sns.set_style("darkgrid")
sns.lmplot(x="average price (unit:10000won)", y="middle school rating", data= df)
plt.show()
'''
#3. 학군과 평균 매매가 사이의 상관계수 분석 (피어슨 상관계수 이용)

df84 = pd.read_csv('real_deal_84.csv')
'''

corr1 = stats.pearsonr(df84["average price (unit:10000won)"], df84["middle school rating"])

corr2 = stats.pearsonr(df84["average price (unit:10000won)"], df84["high school rating"])

corr3 = stats.pearsonr(df84["average price (unit:10000won)"], df84["middle + high school rating"])

print(corr1, corr2, corr3)

corr4 = stats.pearsonr(df84["top 25% price (unit:10000won)"], df84["middle school rating"])

corr5 = stats.pearsonr(df84["top 25% price (unit:10000won)"], df84["high school rating"])

corr6 = stats.pearsonr(df84["top 25% price (unit:10000won)"], df84["middle + high school rating"])

print(corr4, corr5, corr6)
'''
#4. 직주근접과 평균 매매가 사이의 상관계수 분석 (피어슨 상관계수 이용)
corr1 = stats.pearsonr(df84["average price (unit:10000won)"], df84["Number of jobs by withholding region"])

corr2 = stats.pearsonr(df84["average price (unit:10000won)"], df84["salary per person by withholding region"])

corr3 = stats.pearsonr(df84["average price (unit:10000won)"], df84["salary per person by residence"])

print(corr1, corr2, corr3)

sns.set(style = "darkgrid")

g1 = sns.relplot(x="average price (unit:10000won)", y="salary per person by residence", data= df84, hue ='local_name')

for name in df84.index:
    plt.text(df84["top 25% price (unit:10000won)"][name]*1.01, df84["salary per person by residence"][name], df84['local_name'][name])

plt.show()