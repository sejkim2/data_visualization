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
    '건수': [545, 787, 1108],
    '증가율': [None, 44.4, 40.8]  # 첫 해는 증가율이 없으므로 None
}
df = pd.DataFrame(data)

# 막대 그래프 시각화
plt.figure(figsize=(10, 6))

# 막대 그래프 생성 (모든 막대를 같은 색으로 설정, 두께 조정)
bars = plt.bar(df['연도'], df['건수'], color='#1E90FF', width=0.5, label='PT 피해 건수')  # 레이블 추가

# 수치 추가
for i, bar in enumerate(bars):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{yval}건', ha='center', va='bottom', fontsize=14,
             fontweight='bold')  # y 좌표 증가

# 첫 번째 막대에서 두 번째 막대로의 증가량 및 증가율 표시
if df['증가율'][1] is not None:  # 2020년의 경우
    increase = df['건수'][1] - df['건수'][0]  # 2020년에서 2019년 증가량
    increase_rate = (increase / df['건수'][0]) * 100  # 증가율 계산

    # 화살표 추가 (붉은색으로 변경, 위로 볼록)
    plt.annotate(f"",
                 xy=(bars[1].get_x(), bars[1].get_height()),  # 두 번째 막대의 왼쪽 상단 꼭지점
                 xytext=(bars[0].get_x() + bars[0].get_width(), bars[0].get_height()),  # 첫 번째 막대의 오른쪽 상단 꼭지점
                 arrowprops=dict(arrowstyle='->', color='red', lw=2, connectionstyle="arc3,rad=-0.3"))

    # 증가율 추가 (화살표 위에 표시)
    mid_x = (bars[0].get_x() + bars[0].get_width() + bars[1].get_x()) / 2
    mid_y = (bars[0].get_height() + bars[1].get_height()) / 2
    plt.text(mid_x, mid_y - 60, f"{increase_rate:.1f}% 증가", ha='center', fontsize=12, color='red')  # y 좌표 증가

# 두 번째 막대에서 세 번째 막대로의 증가량 및 증가율 표시
if df['증가율'][2] is not None:  # 2021년의 경우
    increase = df['건수'][2] - df['건수'][1]  # 2021년에서 2020년 증가량
    increase_rate = (increase / df['건수'][1]) * 100  # 증가율 계산

    # 화살표 추가 (붉은색으로 변경, 위로 볼록)
    plt.annotate(f"",
                 xy=(bars[2].get_x(), bars[2].get_height()),  # 세 번째 막대의 왼쪽 상단 꼭지점
                 xytext=(bars[1].get_x() + bars[1].get_width(), bars[1].get_height()),  # 두 번째 막대의 오른쪽 상단 꼭지점
                 arrowprops=dict(arrowstyle='->', color='red', lw=2, connectionstyle="arc3,rad=-0.3"))

    # 증가율 추가 (화살표 위에 표시)
    mid_x = (bars[1].get_x() + bars[1].get_width() + bars[2].get_x()) / 2
    mid_y = (bars[1].get_height() + bars[2].get_height()) / 2
    plt.text(mid_x, mid_y - 60, f"{increase_rate:.1f}% 증가", ha='center', fontsize=12, color='red')  # y 좌표 증가

# 그래프 꾸미기
plt.title('PT 이용계약 관련 피해 현황', fontsize=16)
plt.xlabel('연도', fontsize=14)
plt.ylabel('건수', rotation=0, fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()  # 범례 추가
plt.tight_layout()

# 그래프 출력
plt.show()
