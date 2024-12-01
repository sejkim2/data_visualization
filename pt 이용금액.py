import pandas as pd
import matplotlib.pyplot as plt
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 데이터 설정
data = {
    '금액': ['1만원 이상 3만원 미만', '3만원 이상 5만원 미만', '5만원 이상 7만원 미만',
             '7만원 이상', '무료'],
    '퍼센트': [0.055, 0.247, 0.452, 0.178, 0.068]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 원하는 순서대로 정렬
order = ['무료', '1만원 이상 3만원 미만', '3만원 이상 5만원 미만',
         '5만원 이상 7만원 미만', '7만원 이상']
df['금액'] = pd.Categorical(df['금액'], categories=order, ordered=True)
df = df.sort_values(by='금액')

# 파이 차트 시각화 (라벨을 표시하지 않음)
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(df['퍼센트'], labels=None, autopct='%1.1f%%', startangle=90, counterclock=False,
                                    colors=plt.cm.tab20.colors[:len(df)], textprops={'fontsize': 12})

# 그래프 제목 설정
plt.title('PT 이용 금액 비율 (단위 : %)', fontsize=16, fontweight='bold')

# 범례 추가 (더 왼쪽 상단으로 위치 조정)
plt.legend(handles=wedges, labels=df['금액'].tolist(), title='금액', loc='upper left', bbox_to_anchor=(-0.3, 1.1))

# 그래프 표시
plt.show()
