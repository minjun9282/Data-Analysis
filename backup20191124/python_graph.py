import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

#1. 손익과 상승률 2차원 그래프 그리기

#1-1 전용면적 84
df = pd.read_csv('real_deal_84.csv')

sns.set(style = "darkgrid")

g1 = sns.relplot(x="average return (%)", y="average gain and loss (unit: 10000won)", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["average return (%)"][name]*1.01, df["average gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g2 = sns.relplot(x="average return (%)", y="average gain and loss (unit: 10000won)", data= df, hue ='local_name', size = 'middle school rating')
for name in df.index:
    plt.text(df["average return (%)"][name]*1.01, df["average gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g3 = sns.relplot(x="average return (%)", y="average gain and loss (unit: 10000won)", data= df, hue ='local_name', size = 'high school rating')
for name in df.index:
    plt.text(df["average return (%)"][name]*1.01, df["average gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g4 = sns.relplot(x="average return (%)", y="average gain and loss (unit: 10000won)", data= df, hue ='local_name', size = 'middle + high school rating')
for name in df.index:
    plt.text(df["average return (%)"][name]*1.01, df["average gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g5 = sns.relplot(x="average price (unit:10000won)", y="average return (%)", data= df, hue ='local_name')
for name in df.index:
    plt.text(df["average price (unit:10000won)"][name]*1.01, df["average return (%)"][name], df['local_name'][name])

plt.show()


#1-2 전용 면적 59

sns.set(style = "darkgrid")

df = pd.read_csv('real_deal_59.csv')

g1 = sns.relplot(x="average return (%)", y="average gain and loss (unit: 10000won)", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["average return (%)"][name]*1.01, df["average gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g2 = sns.relplot(x="average return (%)", y="average gain and loss (unit: 10000won)", data= df, hue ='local_name', size = 'middle school rating')
for name in df.index:
    plt.text(df["average return (%)"][name]*1.01, df["average gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g3 = sns.relplot(x="average return (%)", y="average gain and loss (unit: 10000won)", data= df, hue ='local_name', size = 'high school rating')
for name in df.index:
    plt.text(df["average return (%)"][name]*1.01, df["average gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g4 = sns.relplot(x="average return (%)", y="average gain and loss (unit: 10000won)", data= df, hue ='local_name', size = 'middle + high school rating')
for name in df.index:
    plt.text(df["average return (%)"][name]*1.01, df["average gain and loss (unit: 10000won)"][name], df['local_name'][name])

plt.show()

g5 = sns.relplot(x="average price (unit:10000won)", y="average return (%)", data= df, hue ='local_name')
for name in df.index:
    plt.text(df["average price (unit:10000won)"][name]*1.01, df["average return (%)"][name], df['local_name'][name])

plt.show()




#2. 매매평균값과 학군 2차원 그래프 그리기. (data/ 중위값 or 평균값 /middle shcool rating or high school rating or middle + high school rating/에서 값을 바꿔 대입하면 원하는 그래프 얻을 수 있음.)

#2-1 전용면적 84
sns.set(style = "darkgrid")

df = pd.read_csv('real_deal_84.csv')

gm = sns.relplot(x="average price (unit:10000won)", y="middle school rating", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["average price (unit:10000won)"][name]*1.01, df["middle school rating"][name], df['local_name'][name])

plt.show()

sns.set_style("darkgrid")
sns.lmplot(x="average price (unit:10000won)", y="middle school rating", data= df)
plt.show()

gh = sns.relplot(x="average price (unit:10000won)", y="high school rating", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["average price (unit:10000won)"][name]*1.01, df["high school rating"][name], df['local_name'][name])

plt.show()

sns.set_style("darkgrid")
sns.lmplot(x="average price (unit:10000won)", y="high school rating", data= df)
plt.show()

#2-2 전용면적 59

sns.set(style = "darkgrid")

df = pd.read_csv('real_deal_59.csv')

gm = sns.relplot(x="average price (unit:10000won)", y="middle school rating", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["average price (unit:10000won)"][name]*1.01, df["middle school rating"][name], df['local_name'][name])

plt.show()


sns.set_style("darkgrid")
sns.lmplot(x="average price (unit:10000won)", y="middle school rating", data= df)
plt.show()

gh = sns.relplot(x="average price (unit:10000won)", y="high school rating", data= df, hue ='local_name')

for name in df.index:
    plt.text(df["average price (unit:10000won)"][name]*1.01, df["high school rating"][name], df['local_name'][name])

plt.show()

sns.set_style("darkgrid")
sns.lmplot(x="average price (unit:10000won)", y="high school rating", data= df)
plt.show()

#3. 학군과 매매가 사이의 상관계수 분석 (피어슨 상관계수 이용)

df84 = pd.read_csv('real_deal_84.csv')


corr1 = stats.pearsonr(df84["average price (unit:10000won)"], df84["middle school rating"])

corr2 = stats.pearsonr(df84["average price (unit:10000won)"], df84["high school rating"])

corr3 = stats.pearsonr(df84["average price (unit:10000won)"], df84["middle + high school rating"])

print(corr1, corr2, corr3)

corr4 = stats.pearsonr(df84["top 25% price (unit:10000won)"], df84["middle school rating"])

corr5 = stats.pearsonr(df84["top 25% price (unit:10000won)"], df84["high school rating"])

corr6 = stats.pearsonr(df84["top 25% price (unit:10000won)"], df84["middle + high school rating"])

print(corr4, corr5, corr6)

corr10 = stats.pearsonr(df84["bottom 25% price (unit:10000won)"], df84["middle school rating"])

corr11 = stats.pearsonr(df84["bottom 25% price (unit:10000won)"], df84["high school rating"])

corr12 = stats.pearsonr(df84["bottom 25% price (unit:10000won)"], df84["middle + high school rating"])

print(corr10, corr11, corr12)

df59 = pd.read_csv('real_deal_59.csv')


corr100 = stats.pearsonr(df59["average price (unit:10000won)"], df59["middle school rating"])

corr200 = stats.pearsonr(df59["average price (unit:10000won)"], df59["high school rating"])

corr300 = stats.pearsonr(df59["average price (unit:10000won)"], df59["middle + high school rating"])

print(corr100, corr200, corr300)

corr400 = stats.pearsonr(df59["top 25% price (unit:10000won)"], df59["middle school rating"])

corr500 = stats.pearsonr(df59["top 25% price (unit:10000won)"], df59["high school rating"])

corr600 = stats.pearsonr(df59["top 25% price (unit:10000won)"], df59["middle + high school rating"])

print(corr400, corr500, corr600)

corr1000 = stats.pearsonr(df59["bottom 25% price (unit:10000won)"], df59["middle school rating"])

corr1100 = stats.pearsonr(df59["bottom 25% price (unit:10000won)"], df59["high school rating"])

corr1200 = stats.pearsonr(df59["bottom 25% price (unit:10000won)"], df59["middle + high school rating"])

print(corr1000, corr1100, corr1200)

#4. 직주근접과 평균 매매가 사이의 상관계수 분석 (피어슨 상관계수 이용)
corr7 = stats.pearsonr(df84["average price (unit:10000won)"], df84["Number of jobs by withholding region"])

corr8 = stats.pearsonr(df84["average price (unit:10000won)"], df84["salary per person by withholding region"])

corr9 = stats.pearsonr(df84["average price (unit:10000won)"], df84["salary per person by residence"])

print(corr7, corr8, corr9)

corr70 = stats.pearsonr(df59["average price (unit:10000won)"], df59["Number of jobs by withholding region"])

corr80 = stats.pearsonr(df59["average price (unit:10000won)"], df59["salary per person by withholding region"])

corr90 = stats.pearsonr(df59["average price (unit:10000won)"], df59["salary per person by residence"])

print(corr70, corr80, corr90)

#5. 평균 매매가 손익과 평균 상승률 사이의 상관계수 분석
corr777 = stats.pearsonr(df84["average return (%)"], df84["average gain and loss (unit: 10000won)"])
corr888 = stats.pearsonr(df59["average return (%)"], df59["average gain and loss (unit: 10000won)"])

print(corr777, corr888)

#6. 평균 매매가와 평균 상승률 사이의 상관계수 분석

corr7777 = stats.pearsonr(df84["average return (%)"], df84["average price (unit:10000won)"])
corr8888 = stats.pearsonr(df59["average return (%)"], df59["average price (unit:10000won)"])

print(corr7777, corr8888)

#보고서용 기타 함수 그리기
sns.set(style = "darkgrid")

g1 = sns.relplot(x="average price (unit:10000won)", y="salary per person by residence", data= df84, hue ='local_name')

for name in df84.index:
    plt.text(df84["average price (unit:10000won)"][name]*1.01, df84["salary per person by residence"][name], df84['local_name'][name])

plt.show()

sns.set(style = "darkgrid")

g2 = sns.relplot(x="average price (unit:10000won)", y="Number of jobs by withholding region", data= df84, hue ='local_name')

for name in df84.index:
    plt.text(df84["average price (unit:10000won)"][name]*1.01, df84["Number of jobs by withholding region"][name], df84['local_name'][name])

plt.show()

g3 = sns.relplot(x="average price (unit:10000won)", y="salary per person by residence", data= df59, hue ='local_name')

for name in df59.index:
    plt.text(df59["average price (unit:10000won)"][name]*1.01, df59["salary per person by residence"][name], df59['local_name'][name])

plt.show()

g4 = sns.relplot(x="average price (unit:10000won)", y="Number of jobs by withholding region", data= df59, hue ='local_name')

for name in df59.index:
    plt.text(df59["average price (unit:10000won)"][name]*1.01, df59["Number of jobs by withholding region"][name], df59['local_name'][name])

plt.show()
