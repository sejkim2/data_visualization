import pandas as pd
import matplotlib.pyplot as plt
import platform
import os

# Mac에서 한글 폰트 설정 (AppleGothic)
from matplotlib import font_manager

# Mac OS에서 한글 처리
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 엑셀 파일 경로
file_path = '../data/lg twins stat.xlsx'  # 실제 파일 경로로 변경

# 엑셀 파일에서 '중견수' 시트 읽기
df = pd.read_excel(file_path, sheet_name='중견수')

# 데이터 미리 보기
print(df.head())

# 박해민 OPS와 리그 중견수 평균 OPS 컬럼 선택
df = df[['년도', 'ops', '리그 중견수 평균 ops']]

# 차이값 계산 (박해민 OPS - 리그 중견수 평균 OPS)
df['차이'] = df['ops'] - df['리그 중견수 평균 ops']

# 차이값 시각화
plt.figure(figsize=(10, 6))

# 막대 그래프 (차이값)
plt.bar(df['년도'], df['차이'], color='purple', alpha=0.7)

# 그래프 꾸미기
plt.title('박해민 OPS와 리그 중견수 평균 OPS 차이 (2014-2024)', fontsize=14)
plt.xlabel('년도', fontsize=12)
plt.ylabel('차이 (OPS)', fontsize=12)

# 세로 격자선 추가
plt.grid(True, axis='y', linestyle='--', linewidth=0.7)

# X축 년도 단위 설정 (1년 단위로 표시)
plt.xticks(df['년도'], rotation=45)  # 년도를 X축에 표시하고, 각도를 45도로 회전하여 겹침 방지

# 그래프 저장 (파일로 저장)
plt.savefig('박해민_vs_리그_차이(바 차트).png', dpi=300)

# 그래프 출력
plt.show()
