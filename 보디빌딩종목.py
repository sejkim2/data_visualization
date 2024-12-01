import pandas as pd
import matplotlib.pyplot as plt
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# Excel 파일과 시트 이름 설정
file_path = 'data/health.xlsx'
sheet_name = '보디빌딩 종목'  # 원하는 시트 이름

# 특정 시트에서 데이터 읽기
data = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

# 데이터 확인
print(data)

# 라벨과 값 설정
labels = data.iloc[0]  # 첫 번째 행을 라벨로 사용
values = data.iloc[1]  # 두 번째 행을 값으로 사용

# 숫자형으로 변환 (결측치는 NaN으로 처리)
values = pd.to_numeric(values, errors='coerce')

# NaN 값을 제거
labels = labels.dropna()
values = values.dropna()

# 데이터 정렬 (값이 적은 것부터 시계방향으로 정렬)
sorted_data = pd.DataFrame({'Label': labels, 'Value': values})
sorted_data = sorted_data.sort_values(by='Value', ascending=True)

# 정렬된 라벨과 값 추출
sorted_labels = sorted_data['Label'].tolist()
sorted_values = sorted_data['Value'].tolist()

# 색상 설정 (경험 항목은 주황색, 나머지는 회색)
colors = ['orange' if label == '경험' else 'lightgray' for label in sorted_labels]

# 파이 차트 시각화
plt.figure(figsize=(10, 8))
plt.pie(sorted_values, labels=sorted_labels, autopct='%1.1f%%', startangle=90, counterclock=False,
        colors=colors)

# 그래프 제목 설정
plt.title('보디 빌딩 중 부상을 당한 경험 조사', fontsize=16, fontweight='bold')

# 추가 정보 텍스트
plt.text(0, 1.2, '일반국민 3530명, 단위 : %', fontsize=12, ha='center')

# 그래프 표시
plt.show()
