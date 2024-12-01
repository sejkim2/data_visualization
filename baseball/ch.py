import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 데이터 정의
data = {
    '년도': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    '최원태 평균자책점': [7.23, 4.46, 3.95, 3.38, 5.07, 4.58, 3.75, 4.975, 4.26],
    '리그 자책점 평균': [5.29, 4.88, 5.23, 4.2, 4.61, 4.43, 3.9, 4.06, 4.77]
}

# DataFrame 생성
df = pd.DataFrame(data)

# 평균값 계산
mean_최원태 = df['최원태 평균자책점'].mean()
mean_리그 = df['리그 자책점 평균'].mean()

# 시각화
plt.figure(figsize=(12, 6))

# 1. 선 그래프 (최원태 선수와 리그 자책점 평균 비교)
sns.lineplot(x='년도', y='최원태 평균자책점', data=df, marker='o', color='blue', label='최원태 선수 평균자책점', linewidth=2)
sns.lineplot(x='년도', y='리그 자책점 평균', data=df, marker='o', color='orange', label='KBO 리그 평균자책점', linewidth=2)

# 2. 평균값 선 추가 (가로선)
plt.axhline(mean_최원태, color='blue', linestyle='-.', linewidth=3, label=f'최원태 평균: {mean_최원태:.2f}')
plt.axhline(mean_리그, color='orange', linestyle=':', linewidth=3, label=f'리그 평균: {mean_리그:.2f}')

# 3. 평균값 텍스트 추가 (그래프에 값 표시)
# plt.text(2020, mean_최원태 + 0.1, f'{mean_최원태:.2f}', color='blue', fontsize=12, ha='center')
# plt.text(2020, mean_리그 + 0.1, f'{mean_리그:.2f}', color='orange', fontsize=12, ha='center')

# 4. 제목 및 레이블 설정
plt.title('최원태 선수의 평균 자책점(ERA)과 KBO 리그 평균 자책점 비교', fontsize=15)
plt.xlabel('년도', fontsize=12)
plt.ylabel('평균 자책점 (ERA)', fontsize=12)

# 5. 범례 추가
plt.legend()

# 6. 그래프에 격자선 추가 (가로/세로 격자 모두)
plt.grid(True, which='both', axis='both', linestyle='--', linewidth=0.7)

# 7. 그래프 레이아웃 조정
plt.tight_layout()

# plt.savefig('최원태_리그_평균자책점_차이2.png', dpi=300)

# 8. 그래프 출력
plt.show()
