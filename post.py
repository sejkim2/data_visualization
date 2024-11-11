import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 엑셀 파일 경로
file_path = 'data/lg twins stat.xlsx'  # 실제 파일 경로로 변경

# 엑셀 파일에서 '포스트시즌' 시트 읽기
df = pd.read_excel(file_path, sheet_name='포스트시즌')

# 데이터 확인
print(df.head())

# 연도별 평균 자책점 계산 (최원태 선수와 리그 평균)
# 그룹화하여 연도별 평균을 계산
df_avg = df.groupby('년도').agg({
    '평균자책점': 'mean',  # 최원태 선수의 평균 자책점
    '리그 자책점 평균': 'mean'  # 리그의 평균 자책점
}).reset_index()

# 평균값 계산
mean_최원태 = df_avg['평균자책점'].mean()
mean_리그 = df_avg['리그 자책점 평균'].mean()

# 시각화
plt.figure(figsize=(12, 6))

# 1. 선 그래프 (최원태 선수와 리그 자책점 평균 비교)
sns.lineplot(x='년도', y='평균자책점', data=df_avg, marker='o', color='blue', label='최원태 선수 평균자책점', linewidth=2)
sns.lineplot(x='년도', y='리그 자책점 평균', data=df_avg, marker='o', color='orange', label='KBO 리그 평균자책점', linewidth=2)

# 2. 평균값 선 추가 (가로선)
plt.axhline(mean_최원태, color='blue', linestyle='-.', linewidth=3, label=f'최원태 평균: {mean_최원태:.2f}')
plt.axhline(mean_리그, color='orange', linestyle=':', linewidth=3, label=f'리그 평균: {mean_리그:.2f}')

# 3. 평균값 텍스트 추가 (그래프에 값 표시)
# plt.text(2020, mean_최원태 + 0.1, f'{mean_최원태:.2f}', color='blue', fontsize=12, ha='center')
# plt.text(2020, mean_리그 + 0.1, f'{mean_리그:.2f}', color='orange', fontsize=12, ha='center')

# 4. 제목 및 레이블 설정
plt.title('최원태 선수의 포스트시즌 평균 자책점(ERA)과 KBO 리그 평균 포스트시즌 자책점 비교', fontsize=15)
plt.xlabel('년도', fontsize=12)
plt.ylabel('평균 자책점 (ERA)', fontsize=12)

# 5. 범례 추가
plt.legend()

# 6. 그래프에 가로/세로 격자선 추가
plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.7)

# 7. Y축 글자 가로로 설정
plt.yticks(rotation=0)

# 8. 그래프 레이아웃 조정
plt.tight_layout()

# 9. 그래프 저장 (파일로 저장)
plt.savefig('최원태_포스트시즌_ERA_차이.png', dpi=300)

# 10. 그래프 출력 (화면에 출력)
plt.show()
