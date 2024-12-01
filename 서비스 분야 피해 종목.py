import pandas as pd
import matplotlib.pyplot as plt
import platform
import os

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 데이터 불러오기
file_path = 'data/health.xlsx'
df = pd.read_excel(file_path, sheet_name='서비스분야 피해다발 품목')

# 데이터 전처리
df.set_index('품목', inplace=True)

# 막대 그래프 시각화
df.T.plot(kind='bar', figsize=(14, 7), width=0.8)

# 그래프 꾸미기
plt.title('년도별 서비스분야 피해다발 상위 10개 품목')  # 제목 변경
plt.xlabel('연도', fontsize=14)
plt.ylabel('건수 (회)', fontsize=14, rotation=0, labelpad=40)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(title='품목', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# 그래프 출력
plt.show()
