import pandas as pd
import matplotlib.pyplot as plt
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# Excel 파일과 시트 이름 설정
file_path = 'data/health.xlsx'
sheet_name = '연도별 헬스장 등록신고'  # 원하는 시트 이름을 입력

# 특정 시트에서 데이터 읽기
data = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

# 데이터 확인
print(data)

# 년도 및 등록수 설정 (데이터의 두 번째 행을 사용)
years = list(data.iloc[0][1:])  # 첫 번째 열은 제외하고 두 번째 행의 데이터 사용
registrations = list(data.iloc[1][1:])  # 첫 번째 열은 제외하고 세 번째 행의 데이터 사용

# 숫자형으로 변환 (결측치는 NaN으로 처리)
registrations = pd.to_numeric(registrations, errors='coerce')

# NaN 값을 제거
years = [year for year, value in zip(years, registrations) if pd.notna(value)]
registrations = [value for value in registrations if pd.notna(value)]

# 시각화
plt.figure(figsize=(14, 7))
plt.plot(years, registrations, marker='o', linestyle='-', color='b', linewidth=2)

# 그래프 제목 및 레이블 설정
plt.title('년도별 헬스장 등록 추이', fontsize=16, fontweight='bold')
plt.xlabel('년도', fontsize=14)
plt.ylabel('등록횟수', fontsize=14, rotation=0)  # Y축 레이블을 가로로 출력

# X축 범위를 데이터의 시작점과 끝점으로 설정
plt.xlim(min(years), max(years))

# 마지막 X값인 "2022년"을 제외하고 라벨 설정
xticks = years[:-1]  # 마지막 항목을 제외한 X축 라벨
plt.xticks(xticks, [f"{year}" for year in xticks], rotation=45)

# 그래프에 그리드 추가
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# 레이아웃 조정
plt.tight_layout()

# 그래프 표시
plt.show()
