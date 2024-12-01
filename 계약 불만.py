import matplotlib.pyplot as plt
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os_system = platform.system()
if os_system == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 데이터 설정
labels = ['계약해지 관련', '계약불이행', '품질·A/S', '부당행위']
sizes = [92.4, 4.4, 2.6, 0.6]  # 비율
colors = ['#FFA500', '#87CEFA', '#9370DB', '#98FB98']  # 색상
explode = (0.1, 0, 0, 0)  # 계약해지 관련 강조

# 파이 차트 생성
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(
    sizes,
    explode=explode,
    colors=colors,
    startangle=90,  # 시계 방향 정렬
    wedgeprops=dict(edgecolor='w')  # 경계선 추가
)

# 범례 추가
ax.legend(
    wedges,
    labels,
    title="항목",
    loc="upper left",
    bbox_to_anchor=(1, 1),
    fontsize=10
)

# 차트 제목 추가
ax.set_title('<헬스장 피해 유형>', fontsize=14)

# 출력
plt.tight_layout()
plt.show()
