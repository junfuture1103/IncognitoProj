import pandas as pd

# 데이터를 로드합니다. 데이터 파일의 경로를 적절하게 지정해야 합니다.
data = pd.read_csv('기업정보요약_train.csv', usecols=[
    'BusinessNum', 'cmpNm', '기업명', 'ceoNm', 'telNo', 'faxTelNo', 'zip', 'adr', 'dtlAdr', 'cmpTypNm', 'cmpSclNm',
    'pbcoGbNm', 'indCd1', 'indNm'
])

print(data.shape)

# 중복 행을 제거합니다.
data = data.drop_duplicates()

# 결과를 출력합니다.
print(data.shape)

# 중복이 제거된 데이터를 CSV 파일로 저장합니다.
data.to_csv('기업정보요약_train_처리완료.csv', index=False)
