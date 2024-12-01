import pandas as pd
import matplotlib.pyplot as plt
import platform
import os

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 데이터 설정
data = {
    '부상 원인': ['사람과 충돌', '주변 시설과 충돌', '운동 장비에 충돌 또는 맞음', '미끄러져 넘어짐',
                  '물체에 걸려 넘어짐', '떨어짐', '점프 후 착지를 잘못함', '무리한 동작', '기타'],
    '생활체육인': [1, 1.4, 6.2, 4.8, 0.7, 0.7, 1.4, 84.2, 7.6]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 막대 그래프 시각화
plt.figure(figsize=(14, 7))
plt.bar(df['부상 원인'], df['생활체육인'], color='skyblue')

# 그래프 제목 및 레이블 설정
plt.title('헬스 중 부상 원인 비율', fontsize=16, fontweight='bold')
plt.xlabel('부상 원인', fontsize=14)
plt.ylabel('비율 (%)', fontsize=14, rotation=0, labelpad=40)  # Y축 레이블과 y축 간 간격을 더 넓게 조정

# X축 라벨 회전
plt.xticks(rotation=45)

# 가로축 및 그래프 그리드 설정
plt.grid(axis='y', linestyle='--', linewidth=0.5)

# 그래프 표시
plt.tight_layout()
plt.show()
