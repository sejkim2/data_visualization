import pandas as pd
import matplotlib.pyplot as plt
import platform
import os
import matplotlib.dates as mdates

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# CSV 파일 읽기
data = pd.read_csv('data/trend.csv', parse_dates=['date'])

# 데이터 확인
print(data.head())

# 데이터 시각화
plt.figure(figsize=(12, 6))
plt.plot(data['date'], data['value'], marker='o', linestyle='-', color='b')

# 그래프 제목 및 레이블 설정
plt.title('구글 트렌드 (주제 : 헬스)')
plt.xlabel('년도')
plt.ylabel('검색량', labelpad=15)  # labelpad를 추가하여 Y축 레이블과 축 간의 간격을 넓힘

# Y축 레이블 가로로 출력
plt.gca().yaxis.label.set_rotation(0)

# X축 날짜 포맷을 1년 단위로 설정
plt.gca().xaxis.set_major_locator(mdates.YearLocator())  # 1년 단위로 눈금 설정
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # 연도 포맷 설정

# X축 눈금 회전 및 레이아웃 조정
plt.xticks(rotation=45)

# 눈금 추가
plt.grid(True)

# 그래프의 여백 조정 (Y축과 Y축 설명 간의 간격을 늘림)
plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)

# X축 범위를 데이터의 시작점과 끝점으로 설정
plt.xlim(data['date'].min(), data['date'].max())

# 그래프 표시
plt.show()
