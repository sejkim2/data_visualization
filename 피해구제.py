import pandas as pd
import matplotlib.pyplot as plt
import platform
import os

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 데이터 생성
data = {
    '연도': ['2019년', '2020년', '2021년'],
    '헬스장 건수': [1926, 3068, 3224],
}
df = pd.DataFrame(data)
df.set_index('연도', inplace=True)

# 선 차트 시각화
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['헬스장 건수'], marker='o', color='blue', label='헬스장 건수', linewidth=2)  # 선 차트 생성

# 수치 추가
# for i, value in enumerate(df['헬스장 건수']):
#     plt.text(i, value, f'{value:,}건', ha='center', va='bottom', fontsize=14)  # 수치를 선 위에 표시

# 그래프 꾸미기
plt.title('헬스장 피해구제 신청 현황', fontsize=16)
plt.xlabel('연도', fontsize=14)
plt.ylabel('건수', fontsize=14, rotation=0, labelpad=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# 그래프 출력
# plt.legend()
plt.show()
