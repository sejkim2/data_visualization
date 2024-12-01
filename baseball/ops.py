import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 엑셀 파일 경로
file_path = '../data/lg twins stat.xlsx'  # 실제 파일 경로로 변경

# 엑셀 파일에서 '최원태' 시트 읽기
df = pd.read_excel(file_path, sheet_name='최원태')

# 데이터 확인 (엑셀 데이터가 잘 읽어졌는지 확인)
print(df.head())

# 시각화
plt.figure(figsize=(12, 6))

# 1. 선 그래프 (최원태 선수와 리그 자책점 평균 비교)
sns.lineplot(x='년도', y='평균자책점', data=df, marker='o', color='blue', label='최원태 선수 평균자책점', linewidth=2)
sns.lineplot(x='년도', y='리그 자책점 평균', data=df, marker='o', color='orange', label='KBO 리그 평균자책점', linewidth=2)

# 2. 제목 및 레이블 설정
plt.title('최원태 선수의 평균 자책점(ERA)과 KBO 리그 평균 자책점 비교', fontsize=15)
plt.xlabel('년도', fontsize=12)
plt.ylabel('평균 자책점 (ERA)', fontsize=12)

# 3. 범례 추가
plt.legend()

# 4. 그래프에 가로/세로 격자선 추가
plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.7)

# 5. Y축 글자 가로로 설정
plt.yticks(rotation=0)

# 6. 그래프 레이아웃 조정
plt.tight_layout()

# 7. 그래프 저장 (파일로 저장)
plt.savefig('최원태_ERA_comparison.png', dpi=300)  # 고해상도로 저장 (300dpi)

# 8. 그래프 출력 (화면에 출력)
plt.show()
