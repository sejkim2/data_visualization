import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform

# Mac에서 한글 폰트 설정 (AppleGothic)
os = platform.system()
if os == 'Darwin':
    plt.rc('font', family='AppleGothic')

# 엑셀 파일 경로
file_path = 'data/lg twins stat.xlsx'  # 실제 파일 경로로 변경

# 엑셀 파일에서 '박해민' 시트 읽기
df = pd.read_excel(file_path, sheet_name='박해민')

# 데이터 확인 (혹시 NaN 값이나 불필요한 데이터가 있는지 점검)
print(df.head())

# 필요한 열들만 선택: '년도', '나이', 'ops', 'war'
df = df[['년도', '나이', 'ops', 'war']]

# NaN 값이 있는 행을 제거 (안전하게 처리)
df = df.dropna(subset=['ops', 'war'])

# X축에 '년도(나이)' 형식으로 표시하기 위해 문자열로 합침
df['년도_나이'] = df['년도'].astype(str) + ' (' + df['나이'].astype(str) + '세)'

# 시각화
plt.figure(figsize=(10, 6))

# 1. OPS 값 시각화 (선 그래프)
sns.lineplot(x='년도_나이', y='ops', data=df, marker='o', color='blue', label='OPS')

# 2. X축 년도 (나이) 1년 단위로 설정
plt.xticks(df['년도_나이'], rotation=45, ha='right')  # X축에 '년도 (나이)' 형식으로 표시

# 3. 세로선 추가 (각 년도에 대해 세로선 그리기)
for i in range(len(df)):
    plt.axvline(x=i, color='gray', linestyle='--', alpha=0.7)

# 4. 그래프 제목 및 레이블 설정
plt.title('박해민 선수의 연도별 OPS 변화', fontsize=15)
plt.xlabel('년도 (나이)', fontsize=12)
plt.ylabel('OPS', fontsize=12, rotation=0, labelpad=15)  # y축 레이블과 축 사이의 여백 추가

# 5. 그리드 추가 (세로 눈금과 함께 표시)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)  # y축에 대해 그리드 추가

# 6. 그래프 출력
plt.tight_layout()

# 7. 파일로 저장 (예: PNG 형식으로 저장)
output_file = '박해민_OPS변화_그래프.png'
plt.savefig(output_file, dpi=300)  # 300dpi 고해상도로 저장
print(f"그래프가 {output_file}로 저장되었습니다.")

# 8. 그래프 화면 출력
plt.show()
