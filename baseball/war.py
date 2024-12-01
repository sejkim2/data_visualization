import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 데이터 프레임 생성
data = {
    '순위': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    '이름': ['오스틴', '홍창기', '박동원', '문보경', '오지환', '신민재', '문성주', '박해민', '구본혁', '김현수'],
    '타율': [0.319, 0.336, 0.272, 0.301, 0.254, 0.297, 0.315, 0.263, 0.257, 0.294],
    'ops': [0.957, 0.857, 0.81, 0.879, 0.761, 0.758, 0.791, 0.695, 0.662, 0.775],
    'WAR': [5.06, 5.06, 4.4, 4.32, 3, 2.64, 2.41, 2.03, 1.29, 1.06]
}

df = pd.DataFrame(data)

# NaN 값이 있는 행을 제거 (안전하게 처리)
df = df.dropna(subset=['ops', 'WAR', '타율'])

# 상관계수 계산
correlation_ops_war = df['ops'].corr(df['WAR'])
correlation_avg_war = df['타율'].corr(df['WAR'])

print(f"OPS와 WAR 간의 상관계수: {correlation_ops_war:.2f}")
print(f"타율과 WAR 간의 상관계수: {correlation_avg_war:.2f}")

# 산점도 및 회귀 직선 시각화
plt.figure(figsize=(14, 7))

# 1. OPS와 WAR 산점도 및 회귀 직선
plt.subplot(1, 2, 1)
sns.scatterplot(x='ops', y='WAR', data=df, color='blue', s=100, alpha=0.7)
sns.regplot(x='ops', y='WAR', data=df, scatter=False, color='red', line_kws={"color": "red", "lw": 2})

# 2. 타율과 WAR 산점도 및 회귀 직선
plt.subplot(1, 2, 2)
sns.scatterplot(x='타율', y='WAR', data=df, color='green', s=100, alpha=0.7)
sns.regplot(x='타율', y='WAR', data=df, scatter=False, color='orange', line_kws={"color": "orange", "lw": 2})

# 3. 각 점에 선수 이름 추가
for i in range(len(df)):
    plt.text(df['ops'][i] + 0.005, df['WAR'][i], df['이름'][i], fontsize=9, ha='left', va='bottom')

# Y축 범위 설정 (두 차트의 Y축을 동일하게 맞추기)
ymin = df['WAR'].min() - 0.5
ymax = df['WAR'].max() + 0.5
plt.subplot(1, 2, 1)
plt.ylim(ymin, ymax)  # OPS와 WAR 그래프의 Y축 범위
plt.subplot(1, 2, 2)
plt.ylim(ymin, ymax)  # 타율과 WAR 그래프의 Y축 범위

# 4. 제목 및 레이블 설정
plt.subplot(1, 2, 1)
plt.title(f'OPS vs WAR (상관계수: {correlation_ops_war:.2f})', fontsize=15)
plt.xlabel('OPS', fontsize=12)
plt.ylabel('WAR', fontsize=12)

plt.subplot(1, 2, 2)
plt.title(f'타율 vs WAR (상관계수: {correlation_avg_war:.2f})', fontsize=15)
plt.xlabel('타율', fontsize=12)
plt.ylabel('WAR', fontsize=12)

# 5. 그래프 레이아웃 여백 조정
plt.subplots_adjust(left=0.08, right=0.92, top=0.92, bottom=0.1)

# 6. 그래프 출력
plt.show()
