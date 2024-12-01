import pandas as pd
import matplotlib.pyplot as plt
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# Excel 파일과 시트 이름 설정
file_path = 'data/health.xlsx'
sheet_name = '송파구 pt 가격 현황'  # 원하는 시트 이름

# 특정 시트에서 데이터 읽기
data = pd.read_excel(file_path, sheet_name=sheet_name, header=0)

# 데이터 확인
print(data)

# 라벨과 값 설정 (헤더를 제외한 데이터 사용)
labels = data['헬스장']  # 헬스장 이름
values = pd.to_numeric(data['가격'], errors='coerce')  # 가격을 숫자로 변환

# NaN 값을 제거
labels = labels.dropna()
values = values.dropna()

# 평균 가격 계산
average_price = values.mean()

# 평균 가격을 약 50000원 형식으로 표시
average_price_approx = '50,000원'  # 원하는 형식으로 설정

# 시각화 설정
plt.figure(figsize=(14, 7))
bars = plt.bar(labels, values, color='skyblue', label='PT 가격')

# 평균 가격을 점선으로 추가
plt.axhline(y=average_price, color='red', linestyle='--', linewidth=2, label=f'평균 가격: {average_price_approx}')

# 평균 가격 위에 텍스트 추가
plt.text(len(labels) - 1, average_price, f'{average_price_approx}', color='red', fontsize=12, va='bottom')

# 그래프 제목 및 레이블 설정
plt.title('송파구 PT 가격 현황', fontsize=16, fontweight='bold')
plt.xlabel('헬스장', fontsize=14)
plt.ylabel('가격 (단위 : 원)', fontsize=14, labelpad=20, rotation=0, ha='right')  # y축 설명 가로로 출력

# X축 라벨 회전
plt.xticks(rotation=45, ha='right')

# 범례 추가
plt.legend()

# 세로 격자만 추가 (가로 격자는 제거)
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5, alpha=0.3)

# 그래프의 공간을 적절히 조정하여 X축 라벨이 잘리지 않도록 설정
plt.tight_layout(pad=5.0)  # 패딩을 조정하여 여유 공간을 추가

# 그래프 표시
plt.show()
